from flask import Flask
from flask import render_template as render
from flask import request
import requests

import webview

app = Flask(__name__)
# app = Flask(__name__, static_folder='./static', template_folder=',/templates')

@app.route('/', methods = ['GET', 'POST'])
def home():

    if request.method == 'GET':       
        return render('index.html')


    if request.form['search']:
        buscar = request.form['search']
        print(buscar)
        url = f'https://api.giphy.com/v1/gifs/search?api_key=bRS6Jts2rgLM8ZjigDBgvjq4XNLUjMoX&limit=24&q={buscar}'
        giphy = requests.get(url)
        dataGiphy = giphy.json()
        # print(dataGiphy)
        return render('index.html', data=dataGiphy['data'])
    else:
        return render('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)

