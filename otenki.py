#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#########################################################################
#
# コロ助が現在の気象情報を教えてくれるスクリプト
#
#########################################################################

import requests
import sys
import shlex
import subprocess
from datetime import datetime

CMD_SAY = '/home/pi/Robot1/ojtalk_korosuke.sh'

def main():
    #say_datetime()
    say_otenki()
    return

def say_datetime():
    d = datetime.now()
    if 4 <= d.hour < 10:
        hello = 'お早うなり、'
    elif 10 <= d.hour < 18:
        hello = 'こんにちはなり、'
    else:
        hello = '今晩はなり、'
    text = '只今の時刻は、%s月%s日、%s時%s分なり' % (d.month, d.day, d.hour, d.minute)
    text = CMD_SAY + ' ' + hello + text
    print(text)
    proc = subprocess.Popen(shlex.split(text))
    proc.communicate()
    return

def say_otenki():
    weather_text = u'%sの天気は%sなり。'
    temperature_text = u'%sの予想最高気温は%s、予想最低気温は%sなり。'
    noinfo = '情報が無い'

    try:
        citycode = sys.argv[1] #第一引数に地域コードを入力して実行すると、その地域の天気を取得する。
    except:
        citycode = '130010' #デフォルトでは（地域コードを指定しなかった場合は）東京の天気を取得する。

    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=%s' %citycode
    response = requests.get(url)
    data = response.json()
    title = data['title'] + '予報なり。'
    forecasts = data['forecasts']

    # TODAY
    cast = forecasts[0]
    try:
        temperature_max = cast['temperature']['max']['celsius'] + '度'
    except:
        temperature_max = noinfo

    try:
        temperature_min = cast['temperature']['min']['celsius'] + '度'
    except:
        temperature_min = noinfo

    today_w_txt = weather_text % (cast['dateLabel'], cast['telop'])
    today_t_txt = temperature_text % (cast['dateLabel'], temperature_max, temperature_min)

    # TOMMOROW
    cast = forecasts[1]
    try:
        temperature_max = cast['temperature']['max']['celsius'] + '度'
    except:
        temperature_max = noinfo

    try:
        temperature_min = cast['temperature']['min']['celsius'] + '度'
    except:
        temperature_min = noinfo

    tommorow_w_txt = weather_text % (cast['dateLabel'], cast['telop'])
    tommorow_t_txt = temperature_text % (cast['dateLabel'], temperature_max, temperature_min)

    # SAY
    weather_str = title + ' ' + today_w_txt + ' ' + today_t_txt + ' ' + tommorow_w_txt + ' ' + tommorow_t_txt
    text = '''%s '%s' ''' % (CMD_SAY, weather_str)
    print(text)
    proc = subprocess.Popen(shlex.split(text))
    proc.communicate()
    return

### Execute
if __name__ == "__main__":
    main()
