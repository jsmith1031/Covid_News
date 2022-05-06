import requests
from bs4 import BeautifulSoup as bs
import csv


import pyttsx3
engine = pyttsx3.init(driverName='nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)


def abc_news():
    # Load the webpage content

    r = requests.get("https://abcnews.go.com/alerts/coronavirus")
    #Parse the page into html for accessing the data
    html = r.content
    soup = bs(html,'html.parser')

    #Finds out the block with headlines in the form of a list
    h = soup.find_all('div', class_='ContentRoll__Headline')


    count = 0
    dic = {}
    ls = []
    for i in h:
        mlink = bs(str(i),'html.parser')
        title = mlink.find('a')
        desc = mlink.find('div',class_='ContentRoll__Desc')


        dic[title.get('href')] = title.string.upper()+"\n \n"+desc.string


        # print(desc.string)
        #
        # print(title.get('href'))
        #
        #
        # print("-----------------------")


    return  dic




