# 【番外編】Raspberry Pi 3をPCから操作できるようにする

## SSHでリモート操作
#### 手順
1. SSHの有効化
2. Raspberry PiのIPアドレスを調べる
3. SSHでログインできるか確認する
4. Raspberry PiのIPアドレスを固定化する
5.

###### 1. SSHの有効化
「Menu」→「設定」→「Raspberry Piの設定」→「インターフェイス」→「SSHの有効化（ラジオボタンをクリック）」→ 「OK」

###### 2. Raspberry PiのIPアドレスを調べる
LXTerminalを起動しifconfigと入力してENTER
```
pi@raspberypi:~ $ ifconfig
```

###### 3. SSHでログインできるか確認する
MacのTerminalを起動し、ssh pi@[Raspberry PiのIPアドレス]と入力してENTER
```
YI-no-MacBook-Pro:~ Yusuke$ ssh pi@10.0.0.12
```
初回接続時のみ以下のメッセージが表示されるので、yesと入力する
```
The authenticity of host '10.0.0.12 (10.0.0.12)' can't be established.
ECDSA key fingerprint is SHA256:APj5BZ12TnGLzBJQnvy4u9QfqVZspxscaRS+Wkl4Os8.
Are you sure you want to continue connecting (yes/no)?
```
Raspberry Piのパスワードを求められるので、raspberry（初期設定のままの場合）と入力すると...
```
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.0.0.12' (ECDSA) to the list of known hosts.
pi@10.0.0.12's password:
```
以下のメッセージが表示され
```
The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Jun 26 11:55:37 2016
```
SSH接続に無事成功！
```
pi@raspberrypi:~ $
```

###### 4. Raspberry PiのIPアドレスを固定化する
Raspberry Piは初期状態ではDHCPのため、動的にIPアドレスが割り振られる。
今後はRaspberry Piに電源を挿すだけ（ディスプレイやマウス、キーボードは繋げない）で、MacやPCからリモート操作できるようにしたいので、以下の手順でRaspberry Pi に固定IPアドレスを割り当てることにする。


## VNCを使って画面共有

### 参照サイト
1. [Raspberry Pi に SSH接続する（有線）- Qiita](http://qiita.com/MarieKawasuji/items/6beb87d805b449b8f4e2)
1. [ブラきよのラズベリーパイ - 第3回「SSH」を使って、「Raspberry Pi」を操作する](http://burakiyo.com/raspberry-pi/third.php)
