from telebot import types
from textblob import Word


def who_r_u():
   markup_reply=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
   item_admin=types.KeyboardButton(admin())
   item_polzovatel = types.KeyboardButton(polzovatel())
   item_back=types.KeyboardButton(back())
   markup_reply.add(item_admin,item_polzovatel,item_back)
   return markup_reply



def admin_func():
    markup_reply=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    item_add_site=types.KeyboardButton(add_site())
    item_del_site=types.KeyboardButton(del_site_mess())   
    item_checkupd=types.KeyboardButton(news_on_polito())   
    item_back=types.KeyboardButton(back())
    markup_reply.add(item_add_site,item_del_site,item_checkupd,item_back)   
    return markup_reply

def polzovatel_func():
    markup_reply=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,row_width=2)
    item_checkupd=types.KeyboardButton(news_on_polito())   
    item_back=types.KeyboardButton(back())
    markup_reply.add(item_checkupd,item_back)
    return markup_reply

def news_on_polito():
    text='Новости на polito.uz 🗣'
    return text

def back():
    text="🔙Назад🔙"
    return text

def admin():
    text='Админ👨‍🔧'
    return text

def polzovatel():
    text='Пользователь👨‍💻'
    return text

def add_site():
    text='Добавить сайт➕'
    return text

def del_site_mess():
    text='Удалить сайт➖'
    return text
def text_for_mistakes(news_links,text_to_send):
    text=f'Вот такие ошибки в артикле📬 {news_links}:\n{text_to_send}' 
    return text

def text_to_notify(link):
    text=f'Уведомление на {link}🛎🛎🛎'
    return text

def text_for_mistakes2(word,dict):
    text=f"Не {word} ❌, а {dict[word]} ✅\n"
    return text

def probability():
    float=0.9
    return float

def password_quest():
    text="Ответьте на вопрос Сфинкса!⚖️"'\n''Вчера было, сегодня есть и завтра будет. (Время)'
    return text

def password():
    text="время"
    return text

def intro():
    text='1.Этот бот для проверки ошибок и наличие новостей на polito.uz \n2.Админ может следить за новостями на большем количестве сайтов'
    return text

def question():
    text="Кто вы?🤔"
    return text

def message_for_new_admin():
    text='Админ!Извини, что не узнал тебя сразу😭'
    return text

def ask_what_to_do():
    text="Какую функцию предпочтете?🔬"
    return text

def wrong_password():
    text="Неправильный ответ❌\nПопробуйте еще раз"
    return text

def wrong_link():
    text="Вы ввели неправильную ссылку❌\nПопробуйте ещё раз"
    return text

def ask_link():
    text=f'Пожалуйста напишите название сайта✍️ \nПример:https://polito.uz'
    return text

def ans_link():
    text="Вы получите уведомление когда появится что-то новое!📌"
    return text

def site_deleted():
    text="Сайт удален✅"
    return text

def login_admin():
    text="О, давно тебя не было тут,с возвращением🎉🎉🎉"
    return text

def ask_del_link(text2):
    text=f'Пожалуйста напишите название сайта \nПример:https://polito.uz\nимеющиеся сайты:\n{text2}'
    return text

def time_tosleep():
    time_sleep=int(1)
    return time_sleep


def no_mistakes():
    no_mistakes="Ошибок нету"
    return no_mistakes

def osn_site():
    site="https://polito.uz/news"
    return site
