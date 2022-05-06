import requests
from bs4 import BeautifulSoup as bs
import csv
#FOX NEWS
import pyttsx3
engine = pyttsx3.init(driverName='nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)

def fox_news():

    #Load the webpage content
    r = requests.get("https://www.foxnews.com/category/health/infectious-disease/coronavirus")

    #Parse the page into html for accessing the data
    html = r.content
    soup = bs(html,'html.parser')

    #Finds out the block with headlines in the form of a list
    h = soup.find_all('article', class_='article')

    dic={}
    #Extract the headlines along with the summary and link to access the story
    for i in h:
        mlink = bs(str(i),'html.parser')
        body = mlink.find('div',class_='info')
        te = body.find('h4',class_='title')
        title = te.find('a')
        pp = body.find('p', class_='dek')
        try:
            summary = pp.find('a')
        except AttributeError as error:
            continue

        linnnk = title.get('href')
        ab = "https://www.foxnews.com"+linnnk

        dic[ab] = title.string.upper() + "\n \n"+ summary.string

    return dic



