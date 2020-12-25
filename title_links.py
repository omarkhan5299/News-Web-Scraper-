from bs4 import BeautifulSoup as  soup
from urllib.request import urlopen as uReq
from selenium import webdriver
import numpy

#driver =  webdriver.Chrome()
#driver.get('https://youtube.com')


my_url = 'https://www.economist.com/'
uClient = uReq(my_url)
page_html = uClient.read()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"teaser__text"})
Dict = dict()


for container in containers:
    title = container.h3.span.text
    link = container.findAll("a", {"class": "headline-link"})
    ext = link[0]['href']
    full_link = "www.economist.com"+ext
    Dict.update( {title : full_link})


for title in Dict:
    print(title,":",Dict[title])