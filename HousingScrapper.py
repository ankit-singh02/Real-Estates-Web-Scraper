from email import header
from bs4 import BeautifulSoup
import requests 
from csv import writer

url="https://housing.com/in/buy/new_delhi/new_delhi"
page= requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
lists=soup.find_all('div',class_="css-zrd0bv")

with open('HousingScrapper.csv','w',encoding='utf8',newline='') as f:
    thewriter=writer(f)
    header=['Title','Location','Price','Area']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('div', class_="css-11nfaq3").text.replace('\n', '')
        location = list.find('a', class_="css-16drx2b").text.replace('\n', '')
        price = list.find('div', class_="css-18rodr0").text.replace('\n', '')
        area = list.find('div', class_="css-4z3njv").text.replace('\n', '')

        info=[title,location,price,area]
        print(info)
        thewriter.writerow(info)