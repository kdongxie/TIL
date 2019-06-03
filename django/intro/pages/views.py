from django.shortcuts import render
import random
import math
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def hola(request):
    return render(request, 'hola.html')

def dinner(request):
    menu = ['삼겹살', '치킨', '라면', '짜장면', '짬뽕', '떡뽂이', '피자']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)

def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)

def introduce(request, name, age):
    context = {'name': name, "age": age}
    return render(request, 'introduce.html', context)

# Variable routing을 통해 숫자 2개를 받아 곱셈결과를 출력

def times(request, num1, num2):
    context = {'num1': num1, 'num2': num2, 'num3': num1*num2}
    return render(request, 'times.html', context)
# 반지름 r을 인자로 받아 원의 넓이를 구하시오

def circle(request, r):
    space = math.pi*(r*r)
    context = {'r': r, 'space': space}
    return render(request, 'circle.html', context)

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
    return render(request, 'template_language.html', context)

def birthday(request):
    birthday = datetime.now()
    month = birthday.month
    day = birthday.day
    context = {'birthday': birthday, 'month': month, 'day': day}
    return render(request, 'birthday.html', context)

def throw(request):
    return render(request, 'throw.html')

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
    return render(request, 'catch.html', context)

# lotto / get 으로 가져오기
# get -> 1~45 수 중에서 6개를 뽑아서 리스트로 만들어 넘긴다.
# get -> 사용자로부터 이름을 입력 받아 넘긴다.

def name(request):
    return render(request, 'name.html')

def lotto(request):
    lotto = sorted(random.sample(range(1,45),6))
    name = request.GET.get('name')
    context = {'lotto': lotto, 'name': name}
    return render(request, 'lotto.html', context)

