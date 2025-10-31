import requests, time

URL = "https://vanhwbt-agridoc-ai-backend.hf.space"  # thay bằng link thật của bạn

while True:
    try:
        r = requests.get(URL)
        print(f"[{time.strftime('%H:%M:%S')}] ✅ Ping: {r.status_code}")
    except Exception as e:
        print("❌", e)
    time.sleep(240)  # ping mỗi 4 phút
