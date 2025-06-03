import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import random

user_agents = [
    # Chrome on Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    # Firefox on Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    # Edge on Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    # Chrome on macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    # Safari on macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
]


def check_and_open_link():
    url = "https://ssfinc.ca/food-bank"
    headers = {
        "User-Agent": random.choice(user_agents)
    }

    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"❌ Failed to fetch page: {e}")
        return False

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)

        for link in links:
            href = link['href']
            if "jotform.com" in href and "click here to register" in link.text.lower():
                print(f"✅ Found link: {href}")
                webbrowser.open(href)
                return True

        print("🔍 No registration link found, retrying...")
        return False
    else:
        print(f"⚠️ Failed to fetch page: {response.status_code}")
        return False


# 等待使用者輸入 ok 才開始
input_text = input("🔓 請輸入 'ok' 開始持續檢查註冊頁面（Ctrl+C 可中止）： ").strip().lower()
if input_text == 'ok':
    try:
        while True:
            found = check_and_open_link()
            if found:
                break

            sleep_seconds = random.uniform(0.5, 2)
            print(f"⏳ 等待 {sleep_seconds:.2f} 秒後重試...")
            time.sleep(sleep_seconds)

    except KeyboardInterrupt:
        print("\n⛔️ 手動中止。程式結束。")
else:
    print("❌ 未輸入 'ok'，程式結束。")
