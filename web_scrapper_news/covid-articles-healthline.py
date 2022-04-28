import requests
from bs4 import BeautifulSoup as bs

import pyttsx3
engine = pyttsx3.init(driverName='nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)

r = requests.get("https://www.healthline.com/health-news")
# Parse the page into html for accessing the data
html = r.content
soup = bs(html, 'html.parser')

# Finds out the block with headlines in the form of a list
h = soup.find_all('div', class_='css-8atqhb')

for i in h:
    mlink = bs(str(i), 'html.parser')
    title = mlink.find('h2')
    desc = mlink.find('a',class_='css-2fdibo')
    if ("Pandemic" in title.string) or ("COVID" in title.string) or ("Coronavirus" in title.string) or ("Mask" in title.string):

        print(title.string)
        engine.say(title.string)
        engine.runAndWait()
        print(desc.string)
        engine.say(desc.string)
        engine.runAndWait()
        ak= desc.get('href')
        print("https://www.healthline.com"+ak)
        print("--------------")
