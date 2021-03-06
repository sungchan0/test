from flask import Flask, render_template, jsonify, request, session


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


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

    sign2 = db.sign.find_one({'name' : name_receive})


    if(sign2 is None):
        db.sign.insert_one(sign)
        return jsonify({'result': 'success'})

    else:
        return jsonify({'result': 'fail'})



    # return jsonify({'result': 'success'})

@app.route('/sign', methods=['GET'])
def listing():
    name = request.args.get('name')
    password = request.args.get('password')

    sign = db.sign.find_one({'name': name , 'password': password}, {'_id': 0})

    if(sign is None):
        return jsonify({'result': 'fail'})
    else:
        session['name'] = name
        return jsonify({'result': 'success'})



@app.route('/memo', methods=['POST'])
def memo():
    memo_receive = request.form['memo']
    date_receive = request.form['date']
    name = session['name']


    memo = {'memo': memo_receive, 'date': date_receive, 'name':name}

    db.memo.insert_one(memo)

    return jsonify({'result': 'success'})

@app.route('/memo', methods=['GET'])
def memo2():
    date = request.args.get('date')
    # memo = request.args.get('memo')
    name = session['name'] # TODO: 로그인한 회원정보에 메모를 저장하여 로그인한 정보의 메모만 불러오게 연결할 수 있게 session사용.

    # memo1 = list(db.memo.find({'memo' : memo, 'date': date}, {'_id': 0}))
    # TODO: 아이디를 찾아줘서 그 아이디에 저장된 정보만 출력되게 하기.
    # memo2 = list(db.memo.find({'name' : name, 'date': date}, {'_id': 0}))

    if(date is not ''):
        # TODO: date가 공백이 아니면 'memo'라는 key에서 name과 date를 찾아 화면에 띄워주기.
        memo2 = list(db.memo.find({'name': name, 'date': date}, {'_id': 0}))
        return jsonify({'result' : 'success', 'memo' : memo2})
    else:
        # TODO: date가 공백이면 저장되어 있는 전체메모를 화면에 띄워주기.
        memo2 = list(db.memo.find({'name': name}, {'_id': 0}))
        return jsonify({'result' : 'success', 'memo' : memo2})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)