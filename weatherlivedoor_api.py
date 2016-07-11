import requests
import sys

try: citycode = sys.argv[1] #第一引数に地域コードを入力して実行すると、その地域の天気を取得する。
except: citycode = '130010' #デフォルトでは（地域コードを指定しなかった場合は）東京の天気を取得する。
url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=%s' %citycode

response = requests.get(url)
data = response.json()

print('**************************')
print(data['title'])
print('**************************')
print(data['description']['text'])

for forecast in data['forecasts']:
    print('**************************')
    print(forecast['dateLabel']+'('+forecast['date']+')')
    print(forecast['telop'])
print('**************************')
