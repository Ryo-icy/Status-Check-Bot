# StatusCheckBot
サーバのポートを監視するDiscordBot


## ファイル一覧

### ・config
### ・discordbot.py
### ・webhook
### ・messageid
### ・README.md


## 動作環境

### ・Python3
### ・Pythonパッケージ
### 　＊json
### 　＊datetime
### 　＊requests
### 　＊socket
### ・centos7/Raspbian(RaspberryPi4 RAM8GB)/Macbook Pro 2020
##### ※windowsでも動かせますがサポート範囲外です。


## ユーザが変更する箇所

### ・config
###### 好きな名前とポート番号を記入
###### <好きな名前>,ポート番号
###### ※空白を開けないこと
##### 例
###### Servername,25565
###### Creative,25566


### discordbot.py
###### 絶対パスを指定しないと動かない場合に変更する
###### ８行目のpathにフォルダパスを指定
###### ↑ $ pwdコマンドの結果に / を付け足す
##### 例
###### /opt/MCStatusCheckBot/


### webhook
###### Discordで投稿するチャンネルの設定を開く（管理者権限所持する必要がある）
###### 「連携サービス」→「ウェブフック」を選択
###### 新しいウェブフックを作成、コピーする。名前とアイコンは好きに変更してください。

###### コピーしたウェブフックを張り付ける（URL適当です…申し訳ない）
`https://discrd.com/api/webhooks/5830584734/fdiyIUYUIgoife87868gO`


### ＜オプション＞
###### こちらのファイルを設定すると一度投稿されたメッセージを編集していく形になります。
###### 逆に言うとこちらを設定しないとスクリプトが実行される度に投稿されていきます。

### messageid
###### discordをデベロッパーモードにして投稿されたメッセージのIDをコピーする

##### 例（桁数適当です…申し訳ない）
`89403795082479654`

## Twitter
<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">BungeeCord導入ついでにDiscordでステータスチェックするBot作った。<br><br>今度配布してみようかな…<br>OSはLinux系でPython3インストールしていれば使える。<br><br>まあ、設定には管理者権限必要だけど24時間サーバ開いているならこれあると便利かも…<br><br>cronとかで定時実行する運用方法です。 <a href="https://t.co/alMJ8ttEOU">pic.twitter.com/alMJ8ttEOU</a></p>&mdash; りょう (@_ryo_yt) <a href="https://twitter.com/_ryo_yt/status/1349209685526597637?ref_src=twsrc%5Etfw">January 13, 2021</a></blockquote>
