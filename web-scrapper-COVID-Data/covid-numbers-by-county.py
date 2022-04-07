import requests
from bs4 import BeautifulSoup as bs


#GET COUNTY NAME AS INPUT
countyy = input("Enter county name: ")

#PREPARE THE URL TO ACCESS THE NEWS SITE
u1 = "https://www.nytimes.com/interactive/2021/us/"
u2 = "-virginia-covid-cases.html"
url = u1+countyy+u2
u11= "https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/state/virginia/county/"
url1 = u11+countyy+"-county"

#ACCESS THE WEBSITE
r = requests.get(url)
p = requests.get(url1)

#PARSE THE PAGE INTO HTML TO PROCESS THE DATA
html = r.content
bb= p.content
soup = bs(html,'html.parser')
sp = bs(bb,'html.parser')


# RETRIEVING DAILY CASES FROM USAFACTS WEBSITE
h11 = sp.find('tbody',class_='MuiTableBody-root')

dc = h11.find_all('td',class_='MuiTableCell-root')
print("Today's Cases: ",dc[1].string)
print("Today's Deaths: ",dc[4].string)
print("---------------")


# RETRIEVING 7 DAYS AVERAGE CASES FROM NEWYORK TIMES WEBSITE
h = soup.find('tbody', class_='parent super')
k = soup.find('table',class_='g-table top-summary')
cases = k.find('td',class_='num cases svelte-17z9x2b')
print("7 DAY AVERAGE")
print("Cases : ",cases.string)
hospitalized = k.find('td',class_='num hospitalized svelte-17z9x2b')
print("Hospitalized: ",hospitalized.string)
death = k.find('td',class_='num deaths svelte-17z9x2b')
print("Death: ",death.string)
positivity  = k.find('td',class_='num pct_pos svelte-17z9x2b')
print("Test Positivity: ",positivity.string)







