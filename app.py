from flask import Flask
from flask import request
import wikipedia

app = Flask(__name__) #flask 서버를 사용하겠다

#경로 설정
@app.route('/')
def hello_world():
    return '안드로이드+서버 연동 OK'

@app.route('/one')
def hello_one():
    return 'hello one!'

@app.route('/sum', methods=["POST"])
def hello_sum():
    value1 = int(request.form['num1'])
    value2 = int(request.form['num2'])
    return (str(value1+value2))

@app.route('/wikisearch', methods=["POST", "GET"])
def hello_wiki():
    value1 = (request.form['topic'])
    return (wikipedia.summary(value1, sentences=1))

@app.route('/two')
def hello_two():
    return 'hello two'

#서버 운영
if __name__=="__main__":
    app.run(host='0.0.0.0')