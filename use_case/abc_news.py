import requests
from bs4 import BeautifulSoup as bs
import csv



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
        count +=1
        mlink = bs(str(i),'html.parser')
        title = mlink.find('a')
        desc = mlink.find('div',class_='ContentRoll__Desc')


        print(f"H{count}: {title.string.upper()}")
        print(f"Summary: {desc.string}")
        print(f"Link: {title.get('href')}")

        print("-----------------------")
        if count>5:
            break


abc_news()




