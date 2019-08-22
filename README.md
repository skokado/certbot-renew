# Certbot renew

Let's encrypt で取得したSSL証明書の更新処理。
実行結果(標準出力 / 標準エラー出力)をSlackに通知します。

# 前提条件
- Let's Encrypt で取得したSSL証明書がローカルで管理されていること<br>
※デフォルトの保存先パス
  - 証明書: `/etc/letsencrypt/archive/www.haldata.net/cert1.pem`
  - 中間証明書: `/etc/letsencrypt/archive/www.haldata.net/chain1.pem`
  - 秘密鍵: `/etc/letsencrypt/archive/www.haldata.net/privkey1.pem`
- Webコンテンツが存在すること(例: `/var/www/html`)
- `certbot-auto`コマンドがインストールされていること<br>
[参考]()
- Python3がインストールされていること(例: `/usr/bin/python3`)

# 使用方法

```shell
$ git clone https://github.com/skokado/certbot-renew
$ cd certbot-renew
```

## 設定値変更(お使いの環境に合わせて)
- `main.sh`

```shell
## 変数定義
SLACK_WEBHOOK_URL=https://your.webhook.url # Todo: replace webhook URL
TARGET_DOMAIN=www.example.com # Todo: replace your domain
PYTHON_PATH=/usr/bin/python3

## main
# SSL証明書更新の実行.
res=`certbot-auto renew --force-renew --webroot -w /var/www/your-document-root 2>&1` # Todo: replace documentroot
status=$?

# Webサービスの再起動
# Todo: replace your web service environment(e.g. systemctl reload httpd.service)
```

## cronなどで定期実行
```shell
# 例: 毎月初に実行
00 00 1 * * /bin/bash /.../certbot-renew/main.sh
```
