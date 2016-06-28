# 【番外編】Raspberry Pi 3をリモート操作するナリ！（その２）
Raspberry Piをリモート操作できるようにするナリ！  
[SSHでリモート操作](#SSHでリモート操作)と[IPアドレスの固定](#IPアドレスの固定)と[VNCで画面共有](#VNCで画面共有)の豪華三本立てでお送りするナリ！

<br />
## <a name = "IPアドレスの固定">IPアドレスの固定
Raspberry Piは初期状態ではDHCPのため、動的にIPアドレスが割り振られる。
今後はRaspberry Piに電源を挿すだけ（ディスプレイやマウス、キーボードは繋げない）で、MacやPCからリモート操作できるようにしたいので、以下の手順でRaspberry Pi に固定IPアドレスを割り当てることにする。

#### 手順
1. [ルーターのDHCP割り当て範囲を変更するナリ](#1. ルーターのDHCP割り当て範囲を変更するナリ)
2. [有線LANのIPアドレスを固定するナリ](#2. 有線LANのIPアドレスを固定するナリ)
3. [無線LANのインターフェイスを1つに絞るナリ](#3. 無線LANのインターフェイスを1つに絞るナリ)
4. [無線LAN接続の設定を行うナリ](#4. 無線LAN接続の設定を行うナリ)
5. [無線LANに固定IPアドレスを割り当てるナリ](#5. 無線LANに固定IPアドレスを割り当てるナリ)

<br />
#### <a name = "1. ルーターのDHCP割り当て範囲を変更するナリ">1. ルーターのDHCP割り当て範囲を変更するナリ
デバイスをルーターに接続すると、ルーターはDHCPでデバイスにIPアドレスを割り当てるナリ。このIPアドレスは適当なアドレスが割り当てられるわけではないナリ。ルーターは特定の範囲内のIPアドレスを各デバイスに割り当てているナリよ。Raspberry PiのIPアドレスを固定するためには、このDHCP割り当ての範囲外のIPアドレスを与えてあげないといけないナリ。

というわけで、ここではルーターのDHCP割り当て範囲の設定を確認していくナリ！

まずはGoogle Chromeなどのブラウザを起動して、アドレス欄にルーターのIPアドレスを入力するナリ。
`pi@raspberypi:~ $ ifconfig`によるとRaspberry PiのIPアドレスが10.0.0.11なので、ルーターのIPアドレスは10.0.0.1ナリ。

そうするとログイン画面が表示されるナリ。我家ではComcastを使っているので、Comcastのホームページを調べるとUsernameはadmin、Passwordはpasswordと出てくるナリ。

このいい加減なパスワードを入力してログインしたら「Gateway」→「Connection」→「Local IP Network」と進むナリ。
IPv4の欄にDHCP Beginning Address: 10.0.0.2、DHCP Ending Address: 10.0.0.254と書かれているナリ。これが我家のルーターが接続デバイスに自動で割り振るIPアドレスの範囲ナリ。

我輩にはこんなにたくさんのIPアドレスは必要ないので、DHCP Ending Addressを10.0.0.100に変えてしまうナリ。

これで10.0.0.101〜10.0.0.254が固定IPアドレスに使えるようになったナリ！

<br />
#### <a name = "2. 有線LANのIPアドレスを固定するナリ">2. 有線LANのIPアドレスを固定するナリ
固定IPアドレスを割り振れる範囲が分かったところで、手始めに有線LAN接続のIPアドレスを固定してみるナリ。

Raspberry PiをルーターにLANケーブルで接続して起動するナリ。`pi@raspberypi:~ $ ifconfig`によると有線LAN接続の自動割り当てIPアドレスは10.0.0.12だったナリ。ここではこれを10.0.0.102に固定化するナリ。

ホームディレクトリの/etc/network/interfacesというファイルにネットワーク設定が記録されているので、テキストエディタでこれを開くナリ。[<sup>注1</sup>](#注1)
```sh
pi@raspberrypi ~ $ sudo nano /etc/network/interfaces
```

「iface eth0 inet dhcp（またはiface eth0 inet manual）」という行があるので、これを「iface eth0 inet static」に書き換えるナリ。テキストエディタのカーソルは矢印キーで移動できるナリ。
次に、この行の後にIPアドレス、サブネットマスク（さっきのComcastのページに255.255.255.0と書いてあったナリ）、デフォルトゲートウェイ（ルーターのIPアドレスで良いナリ）を入力するナリ。
```
iface eth0 inet static
address 10.0.0.102
netmask 255.255.255.0
gateway 10.0.0.1
```

そしたら編集した内容を保存するナリ。上書き保存するためにはCtrl+o（オー）を押すナリ。下の方にファイル名の確認が出てくるので、リターンキーを押すナリ。エディタを終了するためにCtrl+xを押して完了ナリ！

<br />
<a name = "注1">注1. テキストエディタの使い方やディレクトリやファイルの操作については下記のページに詳しく説明されているナリ。
> *― [第12回 Wi-Fi接続設定をする - ツール・ラボ RaspberryPi電子工作入門][] ―*  

<br />
#### <a name = "3. 無線LANのインターフェイスを1つに絞るナリ">3. 無線LANのインターフェイスを1つに絞るナリ
次に無線LANの設定に移るナリ。さっきも出てきたネットワーク設定に関する/etc/network/interfacesというファイルには、wlan0、wlan1の2つの設定が書かれているので、wlan0に絞るナリ。

さっきと同様に、テキストエディタでファイルを開き、
```sh
pi@raspberrypi ~ $ sudo nano /etc/network/interfaces
```

wlan1に関する3行の頭に「#」を付けてコメントアウトするナリ。
```
#allow-hotplug wlan1
#iface wlan1 inet manual
#    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

<br />
#### <a name = "4. 無線LAN接続の設定を行うナリ">4. 無線LAN接続の設定を行うナリ
ここでは、/etc/wpa_supplicant/wpa_supplicant.confに無線LAN接続の設定情報を書き加えていくナリ。
このファイルには無線LANアクセスポイントのSSIDとパスワードを記載することになるナリが、パスワードを直接記入しておくのはちょっと気が引けるナリ。

こんな時に便利なのがwpa_passphraseナリ。これはSSIDとパスワードを指定するとパスワードを16進数64桁という我輩にはとても覚えきれないようなフォーマットに変換してくれるナリ。

wpa_passphraseの使い方はこうナリ`pi@raspberrypi ~ $ wpa_passphrase "SSIDの文字列" "パスワードの文字列"`。出力結果はこんな感じになるナリ。
```
network={
	ssid="SSIDの文字列"
	#psk="パスワードの文字列"
	psk=b9b376a0ce78d485fac613b425498eee9c206d610133fef6f3ceabb39a8d8575 ←（ダミーの結果）
}
```

この{ }内の3行目のpskをコピペすれば良いナリが、面倒くさいから、こんなコマンドを使ってwpa_passphraseの結果を直接wpa_supplicant.confファイルに追記してしまうナリ。
```sh
pi@raspberrypi /etc/wpa_supplicant $ sudo bash -c 'wpa_passphrase "SSIDの文字列" "パスワードの文字列" >> wpa_supplicant.conf'
```
このコマンドの詳しい説明は以下のページを参照するナリ。
> *― [第12回 Wi-Fi接続設定をする - ツール・ラボ RaspberryPi電子工作入門][] ―*  

これでwpa_supplicant.confにssidと（普通の）パスワードと（すごく長い）パスワードが追加されたナリ。普通のパスワードは記載しておきたくないからテキストエディタで修正するナリ。ついでにその他の情報を入力したら、最終的にはこんな感じになるナリ。
```sh
pi@raspberrypi:~ $ sudo cat /etc/wpa_supplicant/wpa_supplicant.conf ←（wpa_supplicant.confファイルの中身を見るコマンド）
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
    ssid="TP-LINK_FB6942" ←（SSIDの文字列）
    psk=***************** ←（パスワードの文字列）
    proto=RSN
    pairwise=CCMP
    key_mgmt=WPA_PSK
    auth_alg=OPEN
}
network={
    ssid="TP-LINK_AE3CB2" ←（SSIDの文字列）
    psk=***************** ←（パスワードの文字列）
    proto=RSN
    pairwise=CCMP
    key_mgmt=WPA_PSK
    auth_alg=OPEN
}
```

これで設定はうまくいっているはずナリ。次のコマンドを順に入力して確認するナリ。
```sh
pi@raspberrypi:~ $ sudo ifconfig wlan0 down ←（無線LAN接続を解除する）
pi@raspberrypi:~ $ sudo ifconfig wlan0 up ←（無線LANに接続する）
pi@raspberrypi:~ $ sudo ifconfig wlan0 ←（無線LAN接続状況の確認）
```

inetアドレスにIPアドレス（10.0.0.11）が出ていれば成功ナリ！

<br />
#### <a name = "5. 無線LANに固定IPアドレスを割り当てるナリ">5. 無線LANに固定IPアドレスを割り当てるナリ
最後に無線LANのIPアドレスを固定化するナリ。無線LANの固定IPアドレスは10.0.0.101にするナリ。

/etc/dhcpcd.confファイルをテキストエディタで開いて、
```sh
pi@raspberrypi:~ $ sudo nano /etc/dhcpcd.conf
```

一番下に下記を追加するナリ。
```
interface wlan0
static ip_address=10.0.0.101/24
static routers=10.0.0.1
static domain_name_servers=10.0.0.1
```

これで完了ナリ！念のためもう一度接続確認をしてみるナリ。
```sh
pi@raspberrypi:~ $ sudo ifconfig wlan0 down
pi@raspberrypi:~ $ sudo ifconfig wlan0 up
pi@raspberrypi:~ $ sudo ifconfig wlan0
```

inetアドレスが 10.0.0.**101** になっていたら成功ナリ！！

<br />

---
### 参照サイト
1. [第12回 Wi-Fi接続設定をする - ツール・ラボ RaspberryPi電子工作入門][]
1. [MacでRaspberry Piセットアップ(補足) - ツール・ラボ ブログ][]
1. [Raspbian 8.0 (jessie)で無線LANを使う - Qiita yosi-q][]
