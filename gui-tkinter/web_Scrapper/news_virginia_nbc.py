import requests
from bs4 import BeautifulSoup as bs

import pyttsx3
engine = pyttsx3.init(driverName='nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
def news_virginia_nbc():
    r = requests.get("https://www.nbc12.com/health/coronavirus/")
    # Parse the page into html for accessing the data
    html = r.content
    soup = bs(html, 'html.parser')

    # Finds out the block with headlines in the form of a list
    h = soup.find_all('div', class_='headlines | card-title mb-1')
    k = soup.find_all('div',class_='deck | normal font-weight-normal font-weight-normal isText d-block')

    dic = {}
    for i in range(len(h)):
        mlink = bs(str(h[i]), 'html.parser')
        klink = bs(str(k[i]), 'html.parser')
        title = mlink.find('a')
        desc = klink.find('div',class_='w-100')
        link = title.get('href')
        l = "https://www.nbc12.com/"+link
        if title.string is not None:

            dic[l] = title.string.upper() + "\n \n" + desc.string


    return dic
