from django.shortcuts import render
import random
import math
from datetime import datetime
import json
import requests

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def hola(request):
    return render(request, 'pages/hola.html')

def dinner(request):
    menu = ['삼겹살', '치킨', '라면', '짜장면', '짬뽕', '떡뽂이', '피자']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)

def hello(request, name):
    context = {'name': name}
    return render(request, 'pages/hello.html', context)

def introduce(request, name, age):
    context = {'name': name, "age": age}
    return render(request, 'pages/introduce.html', context)

# Variable routing을 통해 숫자 2개를 받아 곱셈결과를 출력

def times(request, num1, num2):
    context = {'num1': num1, 'num2': num2, 'num3': num1*num2}
    return render(request, 'pages/times.html', context)
# 반지름 r을 인자로 받아 원의 넓이를 구하시오

def circle(request, r):
    space = math.pi*(r*r)
    context = {'r': r, 'space': space}
    return render(request, 'pages/circle.html', context)

def template_language(request):
    menus = ['자장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = ['dongxie','justine','mr.huang']
    datetimenow = datetime.now()
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow
    }
    return render(request, 'pages/template_language.html', context)

def birthday(request):
    birthday = datetime.now()
    month = birthday.month
    day = birthday.day
    context = {'birthday': birthday, 'month': month, 'day': day}
    return render(request, 'pages/birthday.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message1 = request.GET.get('message1')
    message2 = request.GET.get('message2')
    message3 = request.GET.get('message3')
    message4 = request.GET.get('message4')
    message5 = request.GET.get('message5')
    context = {'message1': message1,
               'message2': message2,
               'message3': message3,
               'message4': message4,
               'message5': message5,
               }
    return render(request, 'pages/catch.html', context)

# lotto / get 으로 가져오기
# get -> 1~45 수 중에서 6개를 뽑아서 리스트로 만들어 넘긴다.
# get -> 사용자로부터 이름을 입력 받아 넘긴다.

def name(request):
    return render(request, 'pages/name.html')

def lotto(request):
    lotto = sorted(random.sample(range(1,46),6))
    name = request.GET.get('name')
    context = {'lotto': lotto, 'name': name}
    return render(request, 'pages/lotto.html', context)

def lotto2(request):
    return render(request, 'pages/lotto2.html')

def picklotto(request):
    name = request.GET.get('pages/name')

    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=861'
    res = requests.get(url)
    lotto = json.loads(res.text)
    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])
    picked = sorted(random.sample(range(1,46),6))
    matched = len(set(winner) & set(picked))
    if matched == 6:
        result = '1등입니다. 퇴사각?'
    elif matched ==5:
        result = '3등입니다. 휴가각?'
    elif matched ==4:
        result = '4등입니다. 골든벨각?'
    elif matched ==3:
        result = '5등입니다. 다시구매해요~'
    else:
        result = '6등입니다. 열심히일하세요.'

    context = {'name':name,'result':result,'winner':winner,'picked':picked}

    return render(request, 'pages/picklotto.html', context)

def art(request):
    return render(request, 'pages/art.html')
def result(request):
    # 1. form 테그로 날린 데이터를 받는다.
    word = request.GET.get('word')
    # 2. ASCII API를 통해 보낸 응답 결과를 Text로 fonts에 저장한다.
    url = 'http://artii.herokuapp.com/'
    fonts = requests.get(url+'fonts_list').text
    # 3. fonts(str)를 fonts(list)의 형태로 저장한다.
    fonts = fonts.split('\n')
    # 4. fonts(list)요소중 하나를 선택하여 font에 저장한다.
    font = random.choice(fonts)
    # 5. 사용자에게서 받은 word와 랜덤하게 뽑은 font를 가지고 요청을 보낸다.
    result = requests.get(url+f'make?text={word}&font={font}').text
    context = {'result': result}
    return render(request, 'pages/result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name': name, 'pwd': pwd}
    return render(request, 'pages/user_create.html', context)

def static_example(request):
    return render(request, 'pages/static_example.html')
