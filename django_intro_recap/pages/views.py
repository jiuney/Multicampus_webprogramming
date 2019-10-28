from django.shortcuts import render
import random
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

# throw & catch 연습
def throw(request):
    return render(request, 'throw.html')

def catch(request):

    print(request)
    print(request.scheme)
    print(request.path)
    print(request.method)
    print(request.headers)
    print(request.META)
    print(request.GET)

    message = request.GET.get("message")
    message2 = request.GET.get("message2")
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'catch.html', context)

# 로또 번호 추첨
def lotto_pick(request):
    return render(request, 'lotto_pick.html')

def lotto_get(request):
    lottos = range(1, 46)
    pick = random.sample(lottos, 6)
    name = request.GET.get("name")

    context = {
        'name': name,
        'pick': pick
    }
    return render(request, 'lotto_get.html', context)

# 실제 로또 번호로 당첨 확인하기
def lottery(request):
    return render(request, 'lottery.html')

def jackpot(request):
    
    # 1. 사용자의 이름을 받아오자.
    name = request.GET.get("name")
    
    # 2. 나눔로또 API로 요청을 보내 결과 받기
    res = requests.get("https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=882")
    res = res.json()

    # 3. 로또 당첨번호 6개를 골라 winner 리스트에 담자!
    winner = []
    for i in range(1, 7):
        winner.append(res[f'drwtNo{i}'])

    # 4. 1~45 까지의 수 중에서 6개를 뽑아 리스트에 담자

    # 5. set를 활용해 교집합 연산을 활용, 실제 로또 당첨 번호와 컴시기가 뽑아준 번호의 개수 구하기

    # 6. 매칭 결과에 따라 다른 응답 메세지 나타내기 (보너스 번호 제외)

    # 7. 딕셔너리를 넘기자!
    
    context = {}
    return render(request, 'jackpot.html', context)