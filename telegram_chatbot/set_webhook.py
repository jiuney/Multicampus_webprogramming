# set_webhook.py
# 웹훅은 한 번만 걸어주면 되기 때문에, 별도의 파일로 분리해서 관리할게요.
from decouple import config
import requests

token = config("TOKEN")
api_url = f"https://api.telegram.org/bot{token}"
set_webhook_url = f"{api_url}/setWebhook?url=https://ericByHPHK.pythonanywhere.com/710885806:AAEGQ19_8W5IEuvPD1X_YfdL2F-geC3MXn4"

response = requests.get(set_webhook_url)
print(response.text)