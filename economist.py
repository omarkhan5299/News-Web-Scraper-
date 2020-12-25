from bs4 import BeautifulSoup as  soup
from urllib.request import urlopen as uReq
from selenium import webdriver

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

i = 1
for title in Dict:
    
    print(str(i)+"."+title)
    i=i+1

opt = input("Enter the number of the article you want to read?")
i = 1
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://hidester.com/proxy/')
driver.implicitly_wait(10)
searchbox = driver.find_element_by_xpath('//*[@id="input"]')
driver.implicitly_wait(10)

for title in Dict:
    if int(opt) == i:
        print(str(i)+"."+title)
        searchbox.send_keys(Dict[title])
        searchbutton = driver.find_element_by_xpath('//*[@id="hidester-form"]/div/div[2]/input[3]')
        searchbutton.click()
    i=i+1


