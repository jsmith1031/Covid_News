import requests
from bs4 import BeautifulSoup as bs


# function that returns a dictionary containing headline,summary and link 
def covid_articles():
    
    #Load the webpage
    r = requests.get("https://www.healthline.com/health-news")
    # Parse the page into html for accessing the data
    html = r.content
    soup = bs(html, 'html.parser')

    # Finds out the block with headlines in the form of a list
    h = soup.find_all('div', class_='css-8atqhb')
    dic = {}
    for i in h:
        mlink = bs(str(i), 'html.parser')
        title = mlink.find('h2')
        desc = mlink.find('a',class_='css-2fdibo')
        if ("Pandemic" in title.string) or ("COVID" in title.string) or ("Coronavirus" in title.string) or ("Mask" in title.string):


            ak= desc.get('href')
            lk = "https://www.healthline.com"+ak
            
            #update the dictionary with headline, summary and link
            dic[lk] = title.string.upper() + "\n \n" + desc.string

    return dic
