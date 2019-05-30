from flask import Flask, requests
import random
from decouple import config
token = config('TELE_TOKEN')
api_url = f'https://api.telegram.org/bot{token}'
chat_id = config('TELE_ID')# 본인의 telegram 계정 id
# CASE1
#text = input("메세지를 입력하세요: ")
# CASE2
text = random.sample(range(1,46),6)
response = requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')

# terminal에서 telegram.py 실행
# 메세지를 입력하면 telegram에 보내지게 된다.

