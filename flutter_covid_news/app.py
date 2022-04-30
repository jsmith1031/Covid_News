from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
#def hello_world():
def about():
    #return '<h1 style=font-size:200px>This webpage works!!!</h1>'
    json_file = {}
    json_file['query'] = 'hello_world'
    return jsonify(json_file)


if __name__ == '__main__':
    #app.run(host='192.168.1.215', port=5000, debug=True, threaded=False)
    #app.debug = True
    #app.run(host="0.0.0.0") #host="0.0.0.0" will make the page accessable
                            #by going to http://[ip]:5000/ on any computer in 
                            #the network.

    #app.run(port=5000, debug=True, host='0.0.0.0')
    app.run()