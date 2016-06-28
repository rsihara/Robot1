# 【番外編】Raspberry Pi 3をリモート操作するナリ！（その２）
Raspberry Piをリモート操作できるようにするナリ！  
[SSHでリモート操作](#SSHでリモート操作)と[IPアドレスの固定](#IPアドレスの固定)と[VNCで画面共有](#VNCで画面共有)の豪華三本立てでお送りするナリ！

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
