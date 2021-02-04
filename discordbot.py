# 標準ライブラリをインポート
import json
import datetime
import requests
import socket

# ファイルパス指定
path = ''

# webhookを読み込む
with open(path + 'webhook', encoding='utf-8') as file:
    webhook = file.read().strip('\n')

# メッセージIDを読み込む
with open(path + 'messageid', encoding='utf-8') as file:
    messageid = str(file.read()).strip('\n')

# configを読み込む
with open(path + 'config', encoding='utf-8') as file:
    config = file.read().strip('\n')

Name = []
Port = []

# configデータをNameとPortに分離
for line in config.split('\n'):
    temp = line.split(',')
    Name.append(temp[0])
    Port.append(int(temp[1]))

# ステータス絵文字
running = ':white_check_mark:'
stop = ':x:'

# sockインスタンス作成
socks = []
for i in range(0, len(Name)):
    socks.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

# 現在の時刻を取得
dt_now = datetime.datetime.now()
dt_now = str(dt_now)[:16]
dt_now = dt_now.replace('-', '/')

# ステータスチェック関数
def Status_check():
    result = []
    for i, Server in enumerate(Port):
        res = socks[i].connect_ex(('127.0.0.1', Server))
        if res == 0:
            result.append(running)
        else:
            result.append(stop)
    return result

# メイン関数
def main():
    # ステータスチェック
    res = Status_check()
    mes = {
        "embeds": [
            {
                "title": 'Minecraft Server Status Check',
                "color": 65280,
                "footer": {
                    "text": "last check: {}".format(dt_now)
                }
            }
        ]
    }
    body = [
            {
                'name': '{}'.format(Name[i]),
                'value': '{}'.format(res[i]),
                'inline': True
            }for i in range(len(Name))
        ]
    mes['embeds'][0]['fields'] = body
    header = {'Content-Type': 'application/json'}
    if len(messageid) == 0:
        requests.post(webhook, json.dumps(mes), headers= header)
    requests.patch(webhook + '/messages/' + messageid, json.dumps(mes), headers=header)

if __name__ == '__main__':
    main()
