import json

import requests
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

url = 'https://daryo.uz/sitemaps/map_610.xml'

response = requests.get(url)
response.raise_for_status()

root = ET.fromstring(response.content)

now = datetime.now()
seven_days_ago = now - timedelta(days=7)

ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

recent_urls = []


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


for url_tag in root.findall('ns:url', ns):
    loc = url_tag.find('ns:loc', ns).text
    lastmod_tag = url_tag.find('ns:lastmod', ns)
    if lastmod_tag is not None:
        lastmod_str = lastmod_tag.text
        try:
            lastmod_date = datetime.fromisoformat(lastmod_str.replace('Z', '+00:00')).replace(tzinfo=None)
            if seven_days_ago <= lastmod_date <= now:
                recent_urls.append(loc)
        except ValueError:
            continue
full_data = {
    "source": "daryo.uz",
    "posts": []
}
for url in recent_urls:
    data = {}
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    h1 = soup.find("h1", class_="is-title post-title post-view-title").get_text(strip=True)
    data["title"] = h1

    time = soup.find("time", class_="post-date").text
    x = parse_russian_date(time)
    data["url"] = url
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

with open("daryo_uz.json", mode="w", encoding="utf-8") as file:
    json.dump(full_data, file, indent=4, ensure_ascii=False)
