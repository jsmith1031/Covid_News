import requests
from bs4 import BeautifulSoup as bs
import csv
#Load the webpage content
import pyttsx3
engine = pyttsx3.init(driverName='nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)


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
            engine.say(title.string)
            engine.runAndWait()
            link = mlink.find('a')
            lk = link.get('href')

            if lk[0]=='h':
                print(lk)
            else:
                print("www.cnn.com"+lk)
            print("-----------------------")





