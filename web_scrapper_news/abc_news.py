import requests
from bs4 import BeautifulSoup as bs
import csv
#Load the webpage content

r = requests.get("https://abcnews.go.com/alerts/coronavirus")

#Parse the page into html for accessing the data
html = r.content
soup = bs(html,'html.parser')

#Finds out the block with headlines in the form of a list
h = soup.find_all('div', class_='ContentRoll__Headline')


#Print out the news along with desc and link

for i in h:
    mlink = bs(str(i),'html.parser')
    title = mlink.find('a')
    desc = mlink.find('div',class_='ContentRoll__Desc')
    print(title.string)
    print(desc.string)
    print(title.get('href'))

    print("-----------------------")





