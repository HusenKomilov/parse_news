import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json

today = datetime.today().date()
seven_days_ago = today - timedelta(days=7)
dates = [(seven_days_ago + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(8)]

url_base = "https://lenta.ru"
main_data = {
    "source": "lenta.ru",
    "posts": []
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
    return datetime.strptime(date_str.strip(), "%H:%M, %d %B %Y").strftime("%Y-%m-%d %H:%M")

for date in dates:
    y, m, d = date.split("-")
    for page in range(1, 6):  # Har bir sana uchun maksimal 5 sahifa
        try:
            url = f"https://lenta.ru/{y}/{m}/{d}/page/{page}/"
            res = requests.get(url)
            if res.status_code != 200:
                break

            soup = BeautifulSoup(res.text, "html.parser")
            ul = soup.find("ul", class_="archive-page__container")
            if not ul:
                break

            items = ul.find_all("li", recursive=False)
            if not items:
                break

            for li in items:
                try:
                    a_tag = li.find("a")
                    if not a_tag or not a_tag.get("href"):
                        continue

                    content_url = url_base + a_tag["href"]
                    detail_res = requests.get(content_url)
                    if detail_res.status_code != 200:
                        continue

                    detail_soup = BeautifulSoup(detail_res.text, "html.parser")
                    title_tag = detail_soup.find("span", class_="topic-body__title")
                    time_tag = detail_soup.find("a", class_="topic-header__item topic-header__time")
                    content_div = detail_soup.find("div", class_="topic-body__content")
                    img_tags = detail_soup.find_all("img", class_="picture__image")

                    if not title_tag or not time_tag or not content_div:
                        continue

                    title = title_tag.text.strip()
                    published_data = parse_russian_date(time_tag.text)
                    images = [img["src"] for img in img_tags if img.get("src")]
                    content_text = " ".join(p.text.strip() for p in content_div.find_all("p"))

                    post_data = {
                        "date": date,
                        "title": title,
                        "url": content_url,
                        "published_data": published_data,
                        "content": content_text,
                        "image_url": images
                    }

                    main_data["posts"].append(post_data)
                except:
                    continue
        except:
            break

with open("lenta_archive.json", "w", encoding="utf-8") as file:
    json.dump(main_data, file, ensure_ascii=False, indent=4)
