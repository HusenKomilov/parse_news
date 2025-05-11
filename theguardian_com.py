import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import json

seven_days_ago = datetime.now() - timedelta(days=7)

sitemap_url = "https://www.theguardian.com/sitemaps/news.xml"
response = requests.get(sitemap_url)
response.raise_for_status()

root = ET.fromstring(response.content)

ns = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}

parsed_news = {
    "source": "theguardian.com",
    "posts": []
}
def parse_bst_date(date_str):
    months = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    parts = date_str.split()
    if len(parts) < 5:
        return ""
    day = parts[1]
    month = months.get(parts[2], "01")
    year = parts[3]
    time = parts[4].replace(".", ":")
    return f"{year}-{month}-{day} {time}"

for url in root.findall("ns:url", ns):
    loc = url.find("ns:loc", ns).text
    data  = {}
    req = requests.get(loc).text
    soup = BeautifulSoup(req, "html.parser")
    h1 = soup.find("h1", class_="dcr-u0152o")
    if h1:
        data["title"] = h1.text
    data["url"] = loc
    time = soup.find("span", class_="dcr-u0h1qy")
    if time:
        x = parse_bst_date(time.text)
        data["published_at"] = x
    div_p=soup.find("div", class_="article-body-commercial-selector article-body-viewer-selector dcr-11jq3zt")
    if div_p:
        t = ""
        for i in div_p.find_all("p"):
            t += i.text
        data["content"] = t
    uls = soup.find("ul", class_="dcr-1rrvs2w")
    if uls:
        categories = []
        for li in uls:
            categories.append(li.text)
        data["category"] = categories
    data["image_url"] = []
    data["type"] = "gazeta"
    parsed_news["posts"].append(data)

with open("theguardian_com.json", mode="w", encoding="utf-8") as file:
    json.dump(parsed_news, file, indent=4, ensure_ascii=False)
