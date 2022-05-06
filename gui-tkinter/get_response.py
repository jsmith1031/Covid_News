import random
import abc_news
import cnn_news
import fox_news
import news_virginia_nbc
import covid_articles
import covid_numbers

def get_response(message):
    
    greetings_key= ["hi","hello","hey","Hi","Hey","Hello"]
    greetings = ["Hello Human !","Hi! Human Being !!!"]

    help = ["help", "can you help me", "what can you do", "functions","job","work","help me"]

    functions = ["Provide latest News from different news channels", "Provide articles related to COVID-19",
                 "Provide real time data of COVID-19 cases in your county"]

    function_option = ["news","latest news","information"]

    abc = ["abc","ABC","abc news","ABC news"]
    cnn = ["cnn","CNN","cnn news"]
    fox = ["fox","FOX","fox news"]
    nbc = ["virginia news","nbc","NBC"]
    article = ["covid article","articles","article","latest article"]
    
    cases = ['daily cases','cases','data','update','infected','case','number']


    if message.isnumeric():

        return covid_numbers.covid_numbers(message)


    if message in cases:
        return "Please, enter your five digit zip code to get daily cases update: "

    if message in fox:
        return fox_news.fox_news()


    if message in abc:
        return abc_news.abc_news()

    if message in cnn:
        return cnn_news.cnn_news()

    if message in nbc:
        return news_virginia_nbc.news_virginia_nbc()
    if message in article:
        return covid_articles.covid_articles()


    if message in function_option:
        return "I can provide news from \n\n 1. ABC News \n 2. FOX News \n 3. CNN News \n 4. NBC News (Exclusively for Virginia)"


    if message in greetings_key:
        return random.choice(greetings)

    if message in help:
        return functions
    
    else:
        return "I don't understand ! Sorry !"


