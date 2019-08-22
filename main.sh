#!/bin/bash
# スクリプトのバスに移動
cd `dirname $0`

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

# 実行結果をSlackに通知
${PYTHON_PATH} ./slack_webhook.py ${SLACK_WEBHOOK_URL} ${TARGET_DOMAIN} ${status} "${res}"