import requests
import sys

try: citycode = sys.argv[1] #第一引数に地域コードを入力して実行すると、その地域の天気を取得する。
except: citycode = '130010' #デフォルトでは（地域コードを指定しなかった場合は）東京の天気を取得する。
url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=%s' %citycode

response = requests.get(url)
data = response.json()
forecasts = data['forecasts']
noinfo = '情報がありません'
cast = forecasts[0]
try:
    temperature_min = cast['temperature']['min']['celsius']
except:
    temperature_min = noinfo

print('**************************')
print(data['title'])
print('**************************')
print(data['description']['text'])
print('**************************')
print(temperature_min)
for forecast in data['forecasts']:
    print('**************************')
    print(forecast['dateLabel']+'('+forecast['date']+')')
    print(forecast['telop'])
print('**************************')
