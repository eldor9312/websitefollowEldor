import telebot
from telebot import types
from textsite import get_text
from urllib.request import urlopen, Request
import urllib.request
from httplib2 import get_linkss
import requests
from textblob import Word
import re
import time
import hashlib
from telebot.util import async_dec
from bs4 import BeautifulSoup
import buttons
from buttons import text_for_mistakes,text_to_notify,text_for_mistakes2,probability,password,password_quest,intro,question,message_for_new_admin,ask_what_to_do,wrong_password,wrong_link,ask_link,ans_link,site_deleted,login_admin,ask_del_link,admin,polzovatel,add_site,del_site_mess,back,news_on_polito,who_r_u,admin_func,polzovatel_func,time_tosleep,no_mistakes,osn_site
token=''
bot=telebot.TeleBot(token)
list_of_new=[]
list_of_members=[]
@bot.message_handler(commands=['start','help'])
def get_user_info(message):
  if not message.chat.id in list_of_members:
    list_of_members.append(message.chat.id)
  bot.send_message(message.chat.id,intro())
  bot.send_message(message.chat.id,question(),reply_markup=buttons.who_r_u())

@bot.message_handler(content_types=['text'])
def answer(message):
  if message.text==polzovatel():
    bot.send_message(message.chat.id,ask_what_to_do(),reply_markup=buttons.polzovatel_func())

  if message.text==news_on_polito():
    bot.send_message(message.chat.id,ans_link())
    if not message.chat.id in list_of_new:
        list_of_new.append(message.chat.id)
    if not osn_site() in list_of_added:
        list_of_added.append(osn_site())
    if not len(list_of_new)>1:
        checkupdates(osn_site())

  if message.text==admin() and message.chat.id in list_of_admins:
    bot.send_message(message.chat.id,login_admin())
    bot.send_message(message.chat.id,ask_what_to_do(),reply_markup=buttons.admin_func())

  if message.text==add_site() and message.chat.id in list_of_admins:
    msg=bot.send_message(message.chat.id,ask_link())
    bot.register_next_step_handler(msg,adding_site_to_notify)
  
  if message.text==del_site_mess() and message.chat.id in list_of_admins:
    text2='' 
    for i in list_of_added:
      text2+=f'{i}\n'
    msg=bot.send_message(message.chat.id,ask_del_link(text2))
    bot.register_next_step_handler(msg,del_site)
      
  if message.text==back():
    get_user_info(message)

  if message.text==admin() and message.chat.id not in list_of_admins:
    msg=bot.send_message(message.chat.id,password_quest())
    bot.register_next_step_handler(msg,admin_reg)


def get_the_last_news(url):
    news_links=get_linkss(url)[0]
    text=get_text(news_links)
    dict={}
    text_to_send=''
    for word in text:
        if not re.search('\W',word) and not re.search('^[0-9]',word): #and not re.search('^[A-Z]',i):
           word = Word(word)
           result = word.spellcheck()
           if not result[0][0]==word and float(result[0][1])>probability() and not word==result[0][0]+'s' and not result[0][0]=="Youtube":
              dict[word] = result[0][0]
    for word in dict:
        text_to_send +=text_for_mistakes2(word,dict)
    if not dict=={}:
        for user in list_of_new:
          bot.send_message(user,text_for_mistakes(news_links,text_to_send))
    else:
        for user in list_of_new:
            bot.send_message(user,no_mistakes())


list_of_admins=[]
def admin_reg(message):
  if message.text==back():
    answer(message)
  elif message.text.lower()==password():
    list_of_admins.append(message.chat.id)
    bot.send_message(message.chat.id,message_for_new_admin())
    bot.send_message(message.chat.id,ask_what_to_do(), reply_markup=buttons.admin_func())
  else:
    msg=bot.send_message(message.chat.id,wrong_password())
    bot.register_next_step_handler(msg,admin_reg)

list_of_added=[]
def adding_site_to_notify(message):
  try:
    requests.get(message.text, verify=False)
  except:
    if message.text!=back():  
      bot.send_message(message.chat.id,wrong_link())
      msg=bot.send_message(message.chat.id,ask_link())
      bot.register_next_step_handler(msg,adding_site_to_notify)
    else:
      answer(message)
  else:
    bot.send_message(message.chat.id,ans_link())
    if not message.text in list_of_added:
      list_of_added.append(message.text)
    checkupdates(message.text)
def del_site(message):
  if message.text in list_of_added:
    list_of_added.remove(message.text)
    bot.send_message(message.chat.id,site_deleted())
  elif message.text==back(): 
    answer(message)
  else:
    bot.send_message(message.chat.id,wrong_link())


        
@async_dec()
def checkupdates(link):
    url = Request(link,
        headers={'User-Agent': 'Mozilla/5.0'})  
    response = urlopen(url).read() 
    currentHash = hashlib.sha224(response).hexdigest()
    time.sleep(time_tosleep())
    while link in list_of_added:
        try:
            response = urlopen(url).read()
            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(time_tosleep())
            response = urlopen(url).read()
            newHash = hashlib.sha224(response).hexdigest()
            if newHash == currentHash:
               continue
            else:
              if link==osn_site():
                for i in list_of_new:
                    bot.send_message(i, text_to_notify(link))
                get_the_last_news('https://polito.uz/news')
              else:
                  for i in list_of_members:
                      bot.send_message(i, text_to_notify(link))
              response = urlopen(url).read()
              currentHash = hashlib.sha224(response).hexdigest()
              time.sleep(time_tosleep())
              continue
        except Exception as e:
           print("error")                

bot.polling(none_stop=True,interval=0)
