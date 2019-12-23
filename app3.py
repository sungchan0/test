from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/login')
def home():
   return render_template('ex.html')


@app.route('/sign', methods=['GET'])
def listing():
    name = request.args.get('name')
    password = request.args.get('password')

    sign = db.sign.find_one({'name': name , 'password': password}, {'_id': 0})


    return jsonify({'result': 'success', 'name': sign , 'password': sign})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)