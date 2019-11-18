from bs4 import BeautifulSoup as bs
import requests

url = f'https://finance.naver.com/'

response = requests.get(url).text
soup = bs(response, 'html.parser')

kospi = soup.find('span', {'class': 'num'}).text
print(kospi)