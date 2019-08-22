# coding: utf-8

import sys
import requests, json
from SSLcert_expiration_days import get_expiration_days

def send_webhook(url, domain, status, text):
    color = 'good' if status == 0 else 'danger'
    title = 'SSL証明書更新通知: {}'.format(domain)
    value = text + '\n\n証明書の有効期期間は {}日間です.'.format(get_expiration_days(domain))

    payload = {
    'attachments': [
        {
            'fallback': 'Certbot Notification',
            'color': color,
            'fields': [
                {
                'title': title,
                'value': value
                }
            ]
        }
    ]
    }
    requests.post(url, data = json.dumps(payload))
    return

def generate_webhook_message(status):
    color = 'good' if status == 0 else 'danger'
    title = 'Succeeded certbot-renew' if status == 0 else 'An error occured'
    value = 'Hello.' if status == 0 else 'error'
    return color, title, value

if __name__ == '__main__':
    # 実行時に引数を受け取る. 足りなければ異常終了
    # 1. 通知先のSlack Webhook URL
    # 2. 更新対象ドメイン(www.example.com)
    # 3. 直前コマンドのreturnコード
    # 4. 直前コマンドの標準出力 or 標準エラー出力
    args = sys.argv
    if len(args) - 1 < 3:
        print('引数の数が不正です.')
        sys.exit(1)

    url = args[1]
    domain = args[2]
    status = int(args[3])
    text = args[4]

    send_webhook(url, domain, status, text)