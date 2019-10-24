from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def introduce(request, name, age):
    context = {
        'name': name,
        'age': age
    }
    return render(request, 'pages/introduce.html', context)

def dinner(request):
    menu = ['짜장면', '햄버거', '치킨', '초밥', '김밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)

def image(request):
    return render(request, 'pages/image.html')

def hello(request, name):
    menu = ['짜장면', '햄버거', '치킨', '초밥', '김밥']
    pick = random.choice(menu)
    context = {
        'name': name,
        'pick': pick,
        }
    return render(request, 'pages/hello.html', context)

def times(request, num1, num2):
    num3 = num1*num2
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3
    }
    return render(request, 'pages/times.html', context)

def area(request, r):
    area = (r ** 2)*3.14
    context = {'r': r, 'area': area}
    return render(request, 'pages/area.html', context)

def template_language(request):
    menus = ['짜장면', '시저샐러드', '오트밀', '삼겹살']
    my_sentence = 'Life is short, you need python.'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'pages/template_language.html', context)

'''
실습 #1.
오늘이 내 생일이면 '예' 아니면 '아니요'를 화면에 띄워주세요.
DTL을 이용해주세요!
'''
def isbirth(request):
    today = datetime.today()
    if today.month == 6 and today.date == 11:
        result = True
    else:
        result = False
    context = {'result': result}
    return render(request, 'pages/isbirth.html', context)

'''
실습 #2.
url을 통해 들어오는 문자열이 회문인지 아닌지를 판별해주세요!
'''
def ispal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    context = {'result': result, 'word': word}
    return render(request, 'pages/ispal.html', context)