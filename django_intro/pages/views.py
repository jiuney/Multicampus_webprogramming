from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def introduce(request):
    return render(request, 'pages/introduce.html')

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