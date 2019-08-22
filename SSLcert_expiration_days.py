import ssl, socket
import datetime

def get_expiration_days(domain):
    # 初期化
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domain)
    # 宛先ドメインへのコネクションを生成して証明書を取得
    conn.connect((domain, 443))
    cert = conn.getpeercert()
    # 日付の差分を計算(戻り値がGMT のため、9時間加算する)
    expiration_datetime = datetime.datetime.strptime(cert['notAfter'].replace(' GMT', ''), '%b %d %H:%M:%S %Y')
    return (expiration_datetime + datetime.timedelta(hours=9) - datetime.datetime.now()).days

if __name__ == "__main__":
    domain = 'www.google.com'
    print(domain, expiration_days(domain))
