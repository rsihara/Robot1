#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#########################################################################
#
# 現在時刻をコロ助が教えてくれるスクリプト
#
#########################################################################

import shlex
import subprocess
from datetime import datetime

CMD_SAY = '/home/pi/Robot1/ojtalk_korosuke.sh'

def main():
    say_datetime()
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

### Execute
if __name__ == "__main__":
    main()
