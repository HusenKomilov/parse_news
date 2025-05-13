from bs4 import BeautifulSoup
import requests
import json

full_data = {
    "source": "central-asia.news",
    "posts": []
}

for i in range(1, 10):
    url = f"https://central-asia.news/uzbekistan/page/{i}?ysclid=makplbhx6r289285262"
    req = requests.get(url)

    soup = BeautifulSoup(req.text, "html.parser")

    urls = soup.find_all("h3", class_="entry-title td-module-title")
    for a_url in urls:
        try:
            data = {}
            a_soup = a_url.find("a")['href']
            res = requests.get(a_soup).text
            data_soup = BeautifulSoup(res, "html.parser")

            h1 = data_soup.find("h1", class_="entry-title").text

            text = data_soup.find("div", class_="td-post-content tagdiv-type").get_text(strip=True)

            img = data_soup.find("div", class_="td-post-featured-image").find("a")["href"]
            datetime = data_soup.find("time", class_="entry-date updated td-module-date").text
            categories = data_soup.find_all("li", class_="entry-category")
            category_list = [category.text.strip() for category in categories]
            data["title"] = h1
            data["url"] = a_soup
            data["published_at"] = datetime
            data["content"] = text
            data["category"] = category_list
            data["image_url"] = [img]
            data["type"] = "gazeta"
            full_data["posts"].append(data)
        except Exception as e:
            print(a_url, e)


with open("central_asia_news.json", mode="w", encoding="utf-8") as file:
    json.dump(full_data, file, indent=4, ensure_ascii=False)
