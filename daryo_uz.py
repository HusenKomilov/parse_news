import json

import requests
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://daryo.uz/yangiliklar"
req = requests.get(url).text
# driver.get(url)
# for _ in range(10):
#     try:
#         btn = driver.find_element(By.XPATH, '//*[@id="load-more"]/span')
#         btn.click()
#         time.sleep(2)
#     except:
#         print("Tugma topilmadi yoki yuklab bo‘lingan.")
#         break
#
#
# cards = driver.page_source

soup = BeautifulSoup(req, "html.parser")
h2 = soup.find_all("h2", class_="is-title post-title")
recent_urls = []
for i in h2:
    news_url = f"https://daryo.uz{i.find('a')['href']}/"
    recent_urls.append(news_url)


def parse_russian_date(date_str):
    months = {
        "января": "January", "февраля": "February", "марта": "March",
        "апреля": "April", "мая": "May", "июня": "June",
        "июля": "July", "августа": "August", "сентября": "September",
        "октября": "October", "ноября": "November", "декабря": "December"
    }

    current_year = datetime.now().year

    for ru, en in months.items():
        if ru in date_str:
            date_str = date_str.replace(ru, en)
            break

    date_str = f"{date_str} {current_year}"

    return datetime.strptime(date_str, "%d %B, %H:%M %Y").strftime("%Y-%m-%d %H:%M")


full_data = {
    "source": "daryo.uz",
    "posts": []
}
for data_url in recent_urls:
    try:
        data = {}
        req = requests.get(data_url).text
        soup = BeautifulSoup(req, "html.parser")
        h1 = soup.find("h1", class_="is-title post-title post-view-title").get_text(strip=True)
        data["title"] = h1

        time = soup.find("time", class_="post-date").text
        x = parse_russian_date(time)
        data["url"] = data_url
        data["published_at"] = x
        div_p = soup.find("div",
                          class_="post-content post-content-custom cf entry-content default__section border post-content-voice")

        t = ""
        for i in div_p.find_all("p"):
            t += i.text
        data["content"] = t
        category = soup.find("a", class_="category term-color-1").text
        data["category"] = category
        img_list = []
        for img in div_p.find_all("img"):
            img_list.append(f"https://daryo.uz/{img['src']}")
        data["image_url"] = img_list
        data["type"] = "gazeta"

        full_data["posts"].append(data)
    except Exception as e:
        print(e)
        continue

with open("daryo_uz.json", mode="w", encoding="utf-8") as file:
    json.dump(full_data, file, indent=4, ensure_ascii=False)
