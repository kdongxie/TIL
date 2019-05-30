from flask import Flask, render_template,request
import requests
app = Flask(__name__)

@app.route('/write')
def write():
    return render_template("write.html")

@app.route('/send')
def send():
    token = '883283794:AAHI1ePRBhp4e9x248qMHOfgoci9dNVlM2A'
    api_url = f'https://core.telegram.org/bots/api{token}'
    chat_id = '698392945'# 본인의 telegram 계정 id
    # CASE1
    # text = input("메세지를 입력하세요: ")
    # CASE2
    # text = random.sample(range(1, 46), 6)
    text = request.args.get('message')
    response = requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')
    return f'{text}전송완료'

if __name__ == '__main__':
    app.run(debug=True)