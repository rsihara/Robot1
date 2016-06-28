# 【番外編】Raspberry Pi 3をリモート操作するナリ！（その３）
Raspberry Piをリモート操作できるようにするナリ！  
[SSHでリモート操作](#SSHでリモート操作)と[IPアドレスの固定](#IPアドレスの固定)と[VNCで画面共有](#VNCで画面共有)の豪華三本立てでお送りするナリ！

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
