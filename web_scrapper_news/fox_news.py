import requests
from bs4 import BeautifulSoup as bs
import csv
#FOX NEWS
#import pyttsx3
#engine = pyttsx3.init(driverName='nsss')
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[7].id)

test_articles = []

def fox_news():

    #Load the webpage content
    r = requests.get("https://www.foxnews.com/category/health/infectious-disease/coronavirus")

    #Parse the page into html for accessing the data
    html = r.content
    soup = bs(html,'html.parser')

    #Finds out the block with headlines in the form of a list
    h = soup.find_all('article', class_='article')

    #Extract the headlines along with the summary and link to access the story
    for i in h:
        mlink = bs(str(i),'html.parser')
        body = mlink.find('div',class_='info')
        te = body.find('h4',class_='title')
        title = te.find('a')
        tit = title.string
        #print(tit.upper())
        #engine.say(tit)
        #engine.runAndWait()
        linnnk = title.get('href')
        ab = "www.foxnews.com"

        pp = body.find('p',class_='dek')
        try:
            summary = pp.find('a')
        except AttributeError as error:
            continue

        #print(summary.string)
        #engine.say(summary.string)
        #engine.runAndWait()
        #print(ab + linnnk)
        #print("--------------")
        try:#Making sure both the title and summary are valid, 
            #because there are some exception cases where one of them isnt valid and crashes the program
            titleString = title.string
            bodyText = summary.string
            linkString = (ab + linnnk)
        except:
            titleString = ""
            bodyText = ""

        if bodyText != "":
            article = {
                "title" : titleString,
                "body" : bodyText,
                "link" : linkString,
            }
            test_articles.append(article)

fox_news()

articles = []
for i in test_articles:
    if i not in articles:
        articles.append(i)

def getArticles():
    return articles