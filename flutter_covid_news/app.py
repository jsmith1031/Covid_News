from flask import Flask
from flask import jsonify
import sys
sys.path.append('../')

import web_scrapper_news.nbc_news
import web_scrapper_news.fox_news


app = Flask(__name__)


@app.route('/')
#def hello_world():
def about():
    #return '<h1 style=font-size:200px>This webpage works!!!</h1>'
    json_file = {}
    json_file['nbc_news'] = web_scrapper_news.nbc_news.getArticles()
    json_file['fox_news'] = web_scrapper_news.fox_news.getArticles()
    #json_file['titleString'] = web_scrapper_news.nbc_news.getTitleString()
    return jsonify(json_file)


if __name__ == '__main__':
    #app.run(host="0.0.0.0") #host="0.0.0.0" will make the page accessable
                            #by going to http://[ip]:5000/ on any computer in 
                            #the network.
    app.run()