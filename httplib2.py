from bs4 import BeautifulSoup
from bs4.element import Comment
import requests


def get_linkss(url):
    all_links=[]
    website=requests.get(url, verify=False)
    website_text=website.text
    soup=BeautifulSoup(website_text,'lxml')
    html=soup.find_all('header', class_="blog-entry-header clr")
    for links in html:
        link=links.h2.a['href']
        all_links.append(link)
    return all_links


