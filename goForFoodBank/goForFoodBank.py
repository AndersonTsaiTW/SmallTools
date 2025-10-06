import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
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
        print(response.text)  # 加在 soup = BeautifulSoup(...) 前面
        links = soup.find_all('a', href=True)

        for link in links:
            href = link['href']
            print(f"link.text: {link.text}, href: {href}")  # debug
            if "jotform.com" in href:
                print(f"✅ Found link: {href}")
                webbrowser.open(href)
                return True

        print("🔍 No registration link found, retrying...")
        return False
    else:
        print(f"⚠️ Failed to fetch page: {response.status_code}")
        return False


# 直接啟動檢查迴圈
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
