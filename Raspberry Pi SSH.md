# 【番外編】Raspberry Pi 3をリモート操作するナリ！
Raspberry Piをリモート操作できるようにするナリ！  
[SSHでリモート操作](#SSHでリモート操作)と[IPアドレスの固定](#IPアドレスの固定)と[VNCで画面共有](#VNCで画面共有)の豪華三本立てでお送りするナリ！

<br />
## <a name = "SSHでリモート操作">SSHでリモート操作
#### 手順
1. [SSHを有効化するナリ！](#1. SSHの有効化)
2. [IPアドレスを調べるナリ！](#2. Raspberry PiのIPアドレスを調べる)
3. [SSHでログインするナリ！](#3. SSHでログインできるか確認する)

<br />
#### <a name = "1. SSHの有効化">1. SSHを有効化するナリ！
Raspberry Pi 3は初期設定でSSHが有効化されているが、SSHの有効化の方法は以下の通りである。  
「Menu」→「設定」→「Raspberry Piの設定」→「インターフェイス」→「SSHの有効化（ラジオボタンをクリック）」→ 「OK」

<br />
#### <a name = "2. Raspberry PiのIPアドレスを調べる">2. IPアドレスを調べるナリ！
Raspberry PiのIPアドレスを調べるため、LXTerminalを起動しifconfigと入力してENTER
```sh
pi@raspberypi:~ $ ifconfig
```

すると以下のような結果が表示される。
**eth0** が有線接続、**wlan0** が無線接続に関する情報である。それぞれIPアドレスはinetアドレス: の欄に記載されている。
**lo** はローカルループバックアドレス（自分自身を指し示す特殊なIPアドレス）に関する項目で、どんな装置でも127.0.0.1で固定される。
```
eth0      Link encap:イーサネット  ハードウェアアドレス b8:27:eb:a2:8a:57
          inetアドレス:10.0.0.12 ブロードキャスト:10.0.0.255  マスク:255.255.255.0
          inet6アドレス: 2601:42:1:8f00:336e:bf58:df7b:2a51/64 範囲:グローバル
          inet6アドレス: fe80::b70:55a5:f1:22ba/64 範囲:リンク
          UP BROADCAST RUNNING MULTICAST  MTU:1500  メトリック:1
          RXパケット:7237 エラー:0 損失:0 オーバラン:0 フレーム:0
          TXパケット:6350 エラー:0 損失:0 オーバラン:0 キャリア:0
      衝突(Collisions):0 TXキュー長:1000
          RXバイト:1131873 (1.0 MiB)  TXバイト:3466673 (3.3 MiB)

lo        Link encap:ローカルループバック  
          inetアドレス:127.0.0.1 マスク:255.0.0.0
          inet6アドレス: ::1/128 範囲:ホスト
          UP LOOPBACK RUNNING  MTU:65536  メトリック:1
          RXパケット:136 エラー:0 損失:0 オーバラン:0 フレーム:0
          TXパケット:136 エラー:0 損失:0 オーバラン:0 キャリア:0
      衝突(Collisions):0 TXキュー長:1
          RXバイト:11472 (11.2 KiB)  TXバイト:11472 (11.2 KiB)

wlan0     Link encap:イーサネット  ハードウェアアドレス b8:27:eb:f7:df:02
          inetアドレス:10.0.0.11 ブロードキャスト:10.0.0.255  マスク:255.255.255.0
          inet6アドレス: fe80::97a2:5d01:4094:571f/64 範囲:リンク
          inet6アドレス: 2601:42:1:8f00:a022:4e95:cf0a:12c2/64 範囲:グローバル
          UP BROADCAST RUNNING MULTICAST  MTU:1500  メトリック:1
          RXパケット:8643 エラー:0 損失:7247 オーバラン:0 フレーム:0
          TXパケット:915 エラー:0 損失:0 オーバラン:0 キャリア:0
      衝突(Collisions):0 TXキュー長:1000
          RXバイト:3153580 (3.0 MiB)  TXバイト:177359 (173.2 KiB)

```

<br />
#### <a name = "3. SSHでログインできるか確認する">3. SSHでログインするナリ！
MacからSSH接続するにはTerminalを起動するだけでOKらしい[<sup>注1</sup>](#注1)  
MacのApplication一覧からTerminalを起動し、ssh pi@[Raspberry PiのIPアドレス]と入力してENTER
```sh
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
```sh
pi@raspberrypi:~ $
```

接続を解除したい場合はexitと入力するだけ
```sh
pi@raspberrypi:~ $ exit
```

すると以下のようなメッセージが表示され、元のTerminalの操作に戻る。
```
ログアウト
Connection to 10.0.0.12 closed.
YI-no-MacBook-Pro:~ Yusuke$
```

<br />
<a name = "注1">注1.
WindowsでSSH接続を行うためには[Tera Term](https://osdn.jp/projects/ttssh2/ "Tera Term")や[PuTTY](http://hp.vector.co.jp/authors/VA024651/PuTTYkj.html "PuTTYjp")などのインストールが必要らしい...  
> *― [第16回「Raspberry Pi A+でポータブルラズベリーパイを作ろう！」- IT女子のラズベリーパイ入門奮闘記][] ―*  
> *― [WindowsからPuTTYでRaspberry PiにSSH接続する方法 - darmus.net][] ―*  

<br />

---

<br />
## <a name = "IPアドレスの固定">IPアドレスの固定
Raspberry Piは初期状態ではDHCPのため、動的にIPアドレスが割り振られる。
今後はRaspberry Piに電源を挿すだけ（ディスプレイやマウス、キーボードは繋げない）で、MacやPCからリモート操作できるようにしたいので、以下の手順でRaspberry Pi に固定IPアドレスを割り当てることにする。

#### 手順
1. [ルーターのDHCP割り当て範囲を変更する](#1. ルーターのDHCP割り当て範囲を変更する)
2. [有線LANのIPアドレスを固定する](#2. 有線LANのIPアドレスを固定する)
3. [無線LANのインターフェイスを1つに絞る](#3. 無線LANのインターフェイスを1つに絞る)
4. [無線LAN接続の設定を行う](#4. 無線LAN接続の設定を行う)
5. [無線LANに固定IPアドレスを割り当てる](#5. 無線LANに固定IPアドレスを割り当てる)

<br />
#### <a name = "1. ルーターのDHCP割り当て範囲を変更する">1. ルーターのDHCP割り当て範囲を変更する

<br />
#### <a name = "2. 有線LANのIPアドレスを固定する">2. 有線LANのIPアドレスを固定する

<br />
#### <a name = "3. 無線LANのインターフェイスを1つに絞る">3. 無線LANのインターフェイスを1つに絞る

<br />
#### <a name = "4. 無線LAN接続の設定を行う">4. 無線LAN接続の設定を行う

<br />
#### <a name = "5. 無線LANに固定IPアドレスを割り当てる">5. 無線LANに固定IPアドレスを割り当てる


<br />

---

<br />
## <a name = "VNCで画面共有">VNCで画面共有
SSH接続によってMacからRaspberry Piをリモート操作できるようになった。
しかしコマンドライン操作（CUI）のみでRaspberry Piを操っていくのは、初心者の我々にはややハードルが高い。
そこでデスクトップ操作（GUI）が可能になるVNCを導入することにする。  

> ###### VNCとは？
> **Virtual Network Computing**  
> リモートマシン（Raspberry Pi）のデスクトップ（GUI）を別のマシンから操作できるようにするツール  
> *― [第3回「SSH」を使って、「Raspberry Pi」を操作する - ブラきよのラズベリーパイ][] ―*  

#### 手順
1. [Raspb Pi側にVNCサーバーをインストールする](#1. Raspb Pi側にVNCサーバーをインストールする)
2. [Raspberry Piのポート情報の確認](#2. Raspberry Piのポート情報の確認)
3. [MacからRaspberry PiにVNCで接続する](#3. MacからRaspberry PiにVNCで接続する)

<br />
#### <a name = "1. Raspb Pi側にVNCサーバーをインストールする">1. Raspb Pi側にVNCサーバーをインストールする
まずはRaspberry Pi側にVNCサーバー機能をインストールする必要がある。
今回は「tightvncserver」というパッケージをインストールする。

> tightvncserverとは、いくつかある「VNCツール」の中でも、通信速度の早いツールです。  
> 画像を圧縮して通信するので、画面が若干見づらくなる事もあるようです。  
> *― [第3回「SSH」を使って、「Raspberry Pi」を操作する - ブラきよのラズベリーパイ][] ―*  

せっかくなのでSSHで接続したままでMacから以下のコマンドを入力し、VNCサーバーをインストールする。
```sh
pi@Raspberry:~ $ sudo apt-get update
pi@Raspberry:~ $ sudo apt-get upgrade
pi@Raspberry:~ $ sudo apt-get install tightvncserver
```

続いて以下のコマンドを入力して、インストールしたVNCサーバーを起動する。
```sh
pi@Raspberry:~ $ vncserver
```

すると以下のメッセージが表示されパスワードの設定を求められる。
```
You will require a password to access your desktops.

Password:
Verify:
```

korosukeと入力し（パスワードは表示されない）、ENTER。
確認を求められるので、もう一度korosukeと入力しENTER。
すると以下のメッセージが表示されるので、nと入力しENTER。
```
Would you like to enter a view-only password (y/n)?
```

これでRaspberry Pi側の設定は完了
```
New 'X' desktop is raspberrypi:1

Starting applications specified in /home/pi/.vnc/xstartup
Log file is /home/pi/.vnc/raspberrypi:1.log
```

<br />
#### <a name = "2. Raspberry Piのポート情報の確認">2. Raspberry Piのポート情報の確認
次にRaspberry Pi側でVNC接続を受け付けるポートの情報を確認する。SSH接続から以下のコマンドを入力しENTER
```sh
pi@raspberrypi:~ $ netstat -nlt
```

すると以下のメッセージが表示される。状態がLISTENとなっているポートが生きているポートである。ここではポート番号5901が生きているので、これを利用することにする。
```
稼働中のインターネット接続 (サーバのみ)
Proto 受信-Q 送信-Q 内部アドレス            外部アドレス            状態       
tcp        0      0 0.0.0.0:5901            0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:6001            0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN
```

<br />
#### <a name = "3. MacからRaspberry PiにVNCで接続する">3. MacからRaspberry PiにVNCで接続する
Macは標準でVNCサーバー接続をサポートしている。

「Finder」→「GO」→「Connect to Server...」と移動すると、接続するサーバーのアドレスを確認するウインドウが現れる。

Server Address: の欄に`vnc://10.0.0.12:5901`と入力し（10.0.0.12は自分のRaspberry PiのIPアドレス、5901は先ほど調べたポート番号）、「Connect」ボタンをクリック。

続いてパスワード入力画面が現れるので先ほど設定したパスワード（今回はkorosuke）を入力して、「Connect」ボタンをクリック。

するとMacのデスクトップ上にウインドウが現れ、Raspberry Piのデスクトップが表示される！

これで、CUIとGUIによるRaspberry Piのリモート操作が可能になった！！  
これからはRaspberry Piにディスプレイやキーボード、マウスを接続する必要もなくなり、スッキリ＆ラクチンなり！

<br />

---
### 参照サイト
1. [Raspberry Pi に SSH接続する（有線）- Qiita][]
1. [第3回「SSH」を使って、「Raspberry Pi」を操作する - ブラきよのラズベリーパイ][]
1. [第16回「Raspberry Pi A+でポータブルラズベリーパイを作ろう！」- IT女子のラズベリーパイ入門奮闘記][]
1. [WindowsからPuTTYでRaspberry PiにSSH接続する方法 - darmus.net][]
1. [MacからRaspberry PiにVNCでリモートデスクトップ接続する方法 - darmus.net][]

[Raspberry Pi に SSH接続する（有線）- Qiita]:	http://qiita.com/MarieKawasuji/items/6beb87d805b449b8f4e2	"Qiita"
[第3回「SSH」を使って、「Raspberry Pi」を操作する - ブラきよのラズベリーパイ]:	http://burakiyo.com/raspberry-pi/third.php	"ブラきよのラズベリーパイ"
[第16回「Raspberry Pi A+でポータブルラズベリーパイを作ろう！」- IT女子のラズベリーパイ入門奮闘記]:	http://deviceplus.jp/hobby/raspberrypi_entry_016/	"IT女子のラズベリーパイ入門奮闘記"
[WindowsからPuTTYでRaspberry PiにSSH接続する方法 - darmus.net]:	http://darmus.net/raspberry-pi-ssh-windows-putty/	"darmus.net"
[MacからRaspberry PiにVNCでリモートデスクトップ接続する方法 - darmus.net]:	http://darmus.net/raspberry-pi-mac-vnc/	"darmus.net"
