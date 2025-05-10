import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json
import time

today = datetime.today().date()
seven_days_ago = today - timedelta(days=7)
dates = [(seven_days_ago + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(8)]

url_base = "https://lenta.ru"
main_data = {
    "source": "lenta.ru"
}

def parse_russian_date(date_str):
    months = {
        "января": "January", "февраля": "February", "марта": "March",
        "апреля": "April", "мая": "May", "июня": "June",
        "июля": "July", "августа": "August", "сентября": "September",
        "октября": "October", "ноября": "November", "декабря": "December"
    }
    for ru, en in months.items():
        if ru in date_str:
            date_str = date_str.replace(ru, en)
            break
    return datetime.strptime(date_str, "%H:%M, %d %B %Y").strftime("%Y-%m-%d %H:%M")

all_posts = []

for date in dates:
    year, month, day = date.split("-")
    page = 1
    while True:
        url = f"https://lenta.ru/{year}/{month}/{day}/page/{page}/"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.text, "html.parser")
            ul_tag = soup.find("ul", class_="archive-page__container")

            list_items = ul_tag.find_all("li", recursive=False)

            for li in list_items:
                try:
                    link_tag = li.find("a")
                    if not link_tag or not link_tag.has_attr("href"):
                        continue
                    content_url = url_base + link_tag["href"]
                    data_soup = BeautifulSoup(requests.get(content_url).text, "html.parser")

                    title_tag = data_soup.find("span", class_="topic-body__title")
                    time_tag = data_soup.find("a", class_="topic-header__item topic-header__time")
                    content_div = data_soup.find("div", class_="topic-body__content")
                    img_tags = data_soup.find_all("img", class_="picture__image")

                    if not all([title_tag, time_tag, content_div]):
                        continue

                    title = title_tag.text.strip()
                    published_date = parse_russian_date(time_tag.text.strip())
                    images = [img["src"] for img in img_tags if img.has_attr("src")]
                    content_text = " ".join([p.text.strip() for p in content_div.find_all("p")])

                    post = {
                        "date": date,
                        "title": title,
                        "url": content_url,
                        "published_data": published_date,
                        "content": content_text,
                        "category": [],
                        "image_url": images,
                        "type": "gazeta"
                    }
                    all_posts.append(post)

                except Exception as e:
                    continue

            page += 1

        except Exception as e:
            break

main_data["posts"] = all_posts

with open("lenta_ru.json", mode="w", encoding="utf-8") as file:
    json.dump(main_data, file, indent=4, ensure_ascii=False)

print(f"{len(all_posts)} ta maqola saqlandi.")
