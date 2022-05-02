import requests
from bs4 import BeautifulSoup as bs
import csv
#Load the webpage content
import time #Jeffrey testing some stuff, remove later with sleep method
import pyttsx3
engine = pyttsx3.init(driverName='nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)

test_articles = []

def cnn_news():


    r = requests.get("https://www.cnn.com/specials/world/coronavirus-outbreak-intl-hnk")

    #Parse the page into html for accessing the data
    html = r.content
    soup = bs(html,'html.parser')

    #Finds out the block with headlines in the form of a list
    h = soup.find_all('div', class_='cd__content')



    count = 0
    for i in h:
        count +=1
        mlink = bs(str(i),'html.parser')
        title = mlink.find('span',class_="cd__headline-text")
        if count < 5 or count > 12:
            print(title.string)
            #engine.say(title.string)
            #engine.runAndWait()
            link = mlink.find('a')
            lk = link.get('href')

            if lk[0]=='h':
                print(lk)
            else:
                print("www.cnn.com"+lk)
            
            #Now open the article link and fetch a summary
        
            articleLink = requests.get("https://www.cnn.com"+lk)
            articlehtml = articleLink.content
            articlesoup = bs(articlehtml,'html.parser')
            articleTextButHTML = soup.find_all('div', class_='l-container')
            print(str(articleTextButHTML))

            for a in articleTextButHTML:    
                subSearch = bs(str(a),'html.parser')
                summary = mlink.find('div', class_='zn-body__paragraph')
                print(str(summary))
            #summary = articlesoup.find('p', class_='zn-body__paragraph')
            #print(summary.string)
            print("-----------------------")
            time.sleep(30)

def addArticle():
    try:#Making sure both the title and summary are valid, 
        #because there are some exception cases where one of them isnt valid and crashes the program
        titleString = title.string
        bodyText = summary.string
    except:
        titleString = ""
        bodyText = ""

    for li in mlink.find_all('a'):
        if count==1:
            #print(li.get('href'))
            linkString = li.get('href')
            break
        else:
            count+=1
    if bodyText != "":
        article = {
            "title" : titleString,
            "body" : bodyText,
            "link" : ("www.cnn.com"+lk),
        }
        test_articles.append(article)





cnn_news()

#remove duplicates 
articles = []
for i in test_articles:
    if i not in articles:
        articles.append(i)

def getArticles():
    return articles