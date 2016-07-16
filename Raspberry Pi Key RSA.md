# 【番外編】Raspberry Pi 3に家の外からでもアクセスできるようにするナリ！
前回の[Raspberry Piをリモート操作できるようにするナリ！](/Raspberry Pi SSH_1.md)では同じネットワーク内にある機器（Mac）からRaspberry Piを操作できるようになった。  
今回は外出先からもMacでRaspberry Piにアクセスできるようにする。  

```sh
YI-no-MacBook-Pro:~ Yusuke$ ssh-keygen -t rsa
```

```
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/Yusuke/.ssh/id_rsa):
```

```
Enter passphrase (empty for no passphrase):
```

```
Enter same passphrase again:
```

```
Your identification has been saved in /Users/Yusuke/.ssh/id_rsa.
Your public key has been saved in /Users/Yusuke/.ssh/id_rsa.pub.
The key fingerprint is:
xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx Yusuke@YI-no-MacBook-Pro.local
The key's randomart image is:
+---[RSA 2048]----+
|      oo*B**=    |
|       o o=X     |
|         .O.+    |
|         +oo     |
|        S.*.     |
|       . o =.    |
|        ....O    |
|        .o.B.B   |
|         .+=Eoo  |
+----[SHA256]-----+
```

```sh
YI-no-MacBook-Pro:~ Yusuke$ ls .ssh
```

```sh
YI-no-MacBook-Pro:~ Yusuke$ scp .ssh/id_rsa.pub pi@10.0.0.101:
```

```
pi@10.0.0.101's password:
```

```
id_rsa.pub                                    100%  412     0.4KB/s   00:00
```

```sh
pi@raspberrypi:~ $ mkdir .ssh
```

```sh
pi@raspberrypi:~ $ cat id_rsa.pub >> .ssh/authorized_keys
pi@raspberrypi:~ $ chmod 700 .ssh
pi@raspberrypi:~ $ chmod 600 .ssh/authorized_keys
pi@raspberrypi:~ $ rm id_rsa.pub
pi@raspberrypi:~ $ sudo nano /etc/ssh/sshd_config
```

~~まず接続ポート番号を変更しておきます。~~  
~~Port 22 #初期設定→コメントアウト~~  
~~Port 19877 #変更後のポート番号（参考: http://www.vwnet.jp/mura/PortNumbers/port10000-49151.htm）~~  
**ポート番号を変更するとネットワーク外からの接続ができなかった。恐らくComcastのルーターはSSHのポート番号変更に対応していないと思われる。**  
>[Connecting to Raspberry Pi on Remote Network (XFinity Router) - stackoverflow](http://stackoverflow.com/questions/28004205/connecting-to-raspberry-pi-on-remote-network-xfinity-router)

続いて、rootログインを禁止します。  
PermitRootLogin without-password #初期設定→コメントアウト  
PermitRootLogin no #記入  

次に、公開鍵ファイル認証を有効にします。  
RSAAuthentication yes #初期設定→そのまま  
PubkeyAuthentication yes #初期設定→そのまま  
AuthorizedKeysFile     %h/.ssh/authorized_keys #初期設定→コメントアウト外す  

最後に、パスワード認証を無効にします。  
PasswordAuthentication no #初期設定→コメントアウト外す  
PasswordAuthentication no  



```sh
pi@raspberrypi:~ $ sudo /etc/init.d/ssh restart
```

```
[ ok ] Restarting ssh (via systemctl): ssh.service.
```

```sh
YI-no-MacBook-Pro:~ Yusuke$ ssh -i .ssh/id_rsa -p 19877 pi@10.0.0.101
```

```sh
exit
```

```sh
YI-no-MacBook-Pro:~ Yusuke$ nano .ssh/config
```

```
Host raspi
	HostName 10.0.0.101
	User pi
	Port 19877 #追記：家の環境ではPort 22でないと外部ネットワークからの接続に失敗した。
	IdentityFile ~/.ssh/id_rsa
```

```sh
YI-no-MacBook-Pro:~ Yusuke$ ssh raspi
```


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

Server Address: の欄に`vnc://10.0.0.101:5901`と入力し（10.0.0.101は自分のRaspberry PiのIPアドレス、5901は先ほど調べたポート番号）、「Connect」ボタンをクリック。

続いてパスワード入力画面が現れるので先ほど設定したパスワード（今回はkorosuke）を入力して、「Connect」ボタンをクリック。

するとMacのデスクトップ上にウインドウが現れ、Raspberry Piのデスクトップが表示される！

これで、CUIとGUIによるRaspberry Piのリモート操作が可能になった！！  
これからはRaspberry Piにディスプレイやキーボード、マウスを接続する必要もなくなり、スッキリ＆ラクチンなり！

<br />

---
### 参照サイト
1. [Raspberry Piに公開鍵認証を使ってssh接続する- ツール・ラボ][]
1. [予約済みポート(10000-49151) - MURA's HomePage][]

[Raspberry Piに公開鍵認証を使ってssh接続する- ツール・ラボ]:	https://tool-lab.com/2013/11/raspi-key-authentication-over-ssh/	"ツール・ラボ"
[予約済みポート(10000-49151) - MURA's HomePage]:	http://www.vwnet.jp/mura/PortNumbers/port10000-49151.htm	"MURA's HomePage"
