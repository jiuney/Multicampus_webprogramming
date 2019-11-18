from bs4 import BeautifulSoup as bs
import requests
import datetime

date = 20191115
url = f'https://www.vlive.tv/upcoming?d={date}'

response = requests.get(url).text
soup = bs(response, 'html.parser')
upcoming_list = soup.find('ul', {'class': 'upcoming_list'}).find_all('li')

vlive_events = []

def get_channel(chart):
    channel = chart.find('em', {'class': 'name'})
    channel = channel.text if channel else '-'
    return channel

def get_start_at(chart, date):
    time = f'{date} ' + chart.find('span', {'class': 'time'}).text
    # print(time)
    # start_at = datetime.datetime.strptime(time, '%Y%m%d %I:%M %p')
    return time

def get_title(chart):
    title = chart.find('a', {'class': '_title'})
    title = title.text
    return title

def get_img_url(chart):
    tmp = chart.find('a', {'class': 'thumb _videoThumb'})
    img_url = tmp.find('img')['src']
    return img_url

for chart in upcoming_list:
    vlive_events.append({
        'channel': get_channel(chart),
        'start_at': get_start_at(chart, date),
        'title': get_title(chart),
        'img_url': get_img_url(chart),
    })

print(vlive_events)