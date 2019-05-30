from flask import Flask, request
import requests
import random
from decouple import config
app = Flask(__name__)

token = config('TELE_TOKEN')
api_url = f'https://api.telegram.org/bot{token}'

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
        if text in ['로또', 'lotto', 'Lotto']:
            number = range(1, 45)
            lotto = random.sample(number, 6)
            send_url = f'{api_url}/sendMessage?chat_id={chat_id}/&text={lotto}'
        else:
            send_url = f'{api_url}/sendMessage?chat_id={chat_id}/&text={text}'

    #sendMessage 요청하기
        response = requests.get(send_url)
    return '', 200 # 응답을 할 body의 내용 , status code의 형태

if __name__ == "__main__":
    app.run(debug=True)

# https://ngrok.com/ 외부 서버를 일시적으로 사용 가능케 해주는 서비스