import requests
from bs4 import BeautifulSoup as bs
import csv
#FOX NEWS


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
    print("Title: ",tit.upper())
    linnnk = title.get('href')
    ab = "www.foxnews.com"

    pp = body.find('p',class_='dek')
    summary = pp.find('a')


    print("Summary: ",summary.string)
    print(ab + linnnk)
    print("--------------")

