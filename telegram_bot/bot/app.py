from flask import Flask, request
import requests
import random
from decouple import config
app = Flask(__name__)

token = config('TELE_TOKEN')
api_url = f'https://api.telegram.org/bot{token}'

# Naver
NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
papago_url = 'https://openapi.naver.com/v1/papago/n2mt'


@app.route(f'/{token}', methods=['POST']) # 보안을 끌어올린다.
def telegram():
    # request.arg: GET
    # request.forms: POST
    # print(request.get_json())
    # lotto['key] #=> value key값이 없으면 error 발생
    # lotto.get('key) #=> value key값이 없으면 None 리턴 (선호)
    message = request.get_json().get('message')
    print(message)

        # data 가져오기
    if message is not None:
        chat_id = message.get('from').get('id')
        text = message.get('text')

        # 로또

        if text in ['/로또', '/lotto', '/Lotto']:
            number = range(1, 45)
            text = random.sample(number, 6)

        # 네이버
        # /번역 안녕하세요
        if text[0:5] == '/번역 한':
            headers = {
                'X-Naver-Client-id':NAVER_CLIENT_ID,
                'X-Naver-Client-Secret':NAVER_CLIENT_SECRET
            }
            data ={
                'source': 'ko',
                'target': 'en',
                'text': text[6:]
            }
            papago_res = requests.post(papago_url, headers=headers, data=data)
            text = papago_res.json().get("message").get("result").get("translatedText")

        if text[0:5] == '/번역 중':
            headers = {
                'X-Naver-Client-id':NAVER_CLIENT_ID,
                'X-Naver-Client-Secret':NAVER_CLIENT_SECRET
            }
            data ={
                'source': 'zh-CN',
                'target': 'ko',
                'text': text[6:]
            }
            papago_res = requests.post(papago_url, headers=headers, data=data)
            text = papago_res.json().get("message").get("result").get("translatedText")



        send_url = f'{api_url}/sendMessage?chat_id={chat_id}/&text={text}'


    #sendMessage 요청하기

        response = requests.get(send_url)
    return '', 200 # 응답을 할 body의 내용 , status code의 형태

if __name__ == "__main__":
    app.run(debug=True)

# https://ngrok.com/ 외부 서버를 일시적으로 사용 가능케 해주는 서비스