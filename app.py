from flask import Flask, render_template, jsonify, request


app = Flask(__name__)



import requests
from bs4 import BeautifulSoup


from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('ex.html')

@app.route('/join')
def join():
   return render_template('ex3.html')

@app.route('/diary')
def diary():
   return render_template('ex2.html')


@app.route('/sign', methods=['POST'])
def saving():
    name_receive = request.form['name']
    password_receive = request.form['password']



    sign = {'name' : name_receive, 'password' : password_receive}

    db.sign.insert_one(sign)

    return jsonify({'result': 'success'})

@app.route('/sign', methods=['GET'])
def listing():
    name = request.args.get('name')
    password = request.args.get('password')

    sign = db.sign.find_one({'name': name , 'password': password}, {'_id': 0})

    if(sign is None):
        return jsonify({'result': 'fail'})
    else:
        return jsonify({'result': 'success'})



@app.route('/memo', methods=['POST'])
def memo():
    memo_receive = request.form['memo']
    date_receive = request.form['date']

    memo = {'memo': memo_receive, 'date': date_receive}

    db.memo.insert_one(memo)

    return jsonify({'result': 'success'})

@app.route('/memo', methods=['GET'])
def memo2():
    data = request.args.get('data')
    memo = request.args.get('memo')

    memo1 = db.sign.find_one({'data': data, 'memo': memo}, {'_id': 0})



    return jsonify({'result' : 'success'})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)