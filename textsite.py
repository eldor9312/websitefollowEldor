from bs4 import BeautifulSoup
import urllib.request
import requests

def get_text(url):
    website=requests.get(url, verify=False)
    website_text=website.text
    soup=BeautifulSoup(website_text,'lxml')
    text=soup.find('div', class_="entry-content clr",itemprop='text').text.split()
    return text

