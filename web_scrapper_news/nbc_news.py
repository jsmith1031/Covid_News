import requests
from bs4 import BeautifulSoup as bs
import csv


#NBC NEWS

#Load the webpage content



r = requests.get("https://www.bbc.com/news/coronavirus")

#Parse the page into html for accessing the data
html = r.content
soup = bs(html,'html.parser')

#Finds out the block with headlines in the form of a list
h = soup.find_all('div', class_='gs-c-promo-body')

#Extract the headlines along with the summary and link to access the story
for i in h:
    mlink = bs(str(i),'html.parser')
    title = mlink.find('h3',class_='gs-c-promo-heading__title')
    count = 0
    summary = mlink.find('p',class_='gs-c-promo-summary')
    print(title.string)
    print(summary.string)
    for li in mlink.find_all('a'):
        if count==1:
            print(li.get('href'))
            break
        else:
            count+=1
    print("--------------")

