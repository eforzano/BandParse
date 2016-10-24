try:
    from urllib.request  import urlopen
except ImportError:
    from urllib2 import urlopen
try:
    from urllib.parse  import quote, unquote
except ImportError:
    from urllib2 import quote, unquote
import json
import os
from bandParse import artistparse 
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/bandList', methods=['POST'])
def bandList():
    bandName =  request.form['bandName']
    artistList = artistparse(bandName) 
    return jsonify(artistList)

if __name__ == '__main__':
	app.run(debug=True)