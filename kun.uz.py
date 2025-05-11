from bs4 import BeautifulSoup
import requests
import json

urls = [
    "https://kun.uz/news/category/uzbekiston",
    "https://kun.uz/news/category/jahon",
    "https://kun.uz/news/category/iqtisodiyot",
    "https://kun.uz/news/category/jamiyat",
    "https://kun.uz/news/category/sport",
    "https://kun.uz/news/category/texnologiya",
    "https://kun.uz/news/category/nuqtai-nazar"
]

full_data = {
    "source": "kun.uz",
    "posts": []
}

for url in urls:
    req = requests.get(url).text

    soup = BeautifulSoup(req, "html.parser")
    a = soup.find_all("a", class_="news-page__item l-item")
    for j in a:
        data = {}

        a_url = f"https://kun.uz{j['href']}"
        a_req = requests.get(a_url, "html.parser").text
        a_soup = BeautifulSoup(a_req, "html.parser")
        h1 = a_soup.find("h1", class_="news-inner__content-title").text
        data["title"] = h1
        div_p = a_soup.find("div", class_="news-inner__content-page")
        data["url"] = a_url
        data["published_at"] = ""
        t = ""
        for p in div_p.find_all("p"):
            t += p.text
        data["content"] = t
        cat = a_soup.find("div", class_="news-inner__content-stats")
        span = cat.find("span").text.split("|")[0]
        data["category"] = span
        div_img = a_soup("div", class_="news-inner__content-img")
        img_list = []
        if div_img:
            for img in div_img:
                img_list.append(img.find("img")['src'])

        data["image_url"] = img_list
        data["type"] = "gazeta"
        full_data["posts"].append(data)


with open("kun_uz.json", mode="w", encoding="utf-8") as file:
    json.dump(full_data, file, indent=4, ensure_ascii=False)