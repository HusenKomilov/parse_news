import json
import time
from datetime import datetime

import dateparser
import requests
from bs4 import BeautifulSoup


# from send_data import get_last_news, send_data


class NewsParser:
    def __init__(self, url, selectors):
        self.url = url
        self.selectors = selectors

    @staticmethod
    def save_to_json(data, filename="ozodlik_articles.json"):
        with open("files/" + filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Data saved to {filename}")

    # @staticmethod
    # def kiril_to_lotin(text):
    #     mapping = {
    #         'А': 'A', 'а': 'a',
    #         'Б': 'B', 'б': 'b',
    #         'В': 'V', 'в': 'v',
    #         'Г': 'G', 'г': 'g',
    #         'Д': 'D', 'д': 'd',
    #         'Е': 'E', 'е': 'e',
    #         'Ё': 'Yo', 'ё': 'yo',
    #         'Ж': 'J', 'ж': 'j',
    #         'З': 'Z', 'з': 'z',
    #         'И': 'I', 'и': 'i',
    #         'Й': 'Y', 'й': 'y',
    #         'К': 'K', 'к': 'k',
    #         'Л': 'L', 'л': 'l',
    #         'М': 'M', 'м': 'm',
    #         'Н': 'N', 'н': 'n',
    #         'О': 'O', 'о': 'o',
    #         'П': 'P', 'п': 'p',
    #         'Р': 'R', 'р': 'r',
    #         'С': 'S', 'с': 's',
    #         'Т': 'T', 'т': 't',
    #         'У': 'U', 'у': 'u',
    #         'Ф': 'F', 'ф': 'f',
    #         'Х': 'X', 'х': 'x',
    #         'Ц': 'S', 'ц': 's',
    #         'Ч': 'Ch', 'ч': 'ch',
    #         'Ш': 'Sh', 'ш': 'sh',
    #         'Щ': 'Sh', 'щ': 'sh',
    #         'Ъ': '', 'ъ': '',
    #         'Ы': 'I', 'ы': 'i',
    #
    #         'Ь': '', 'ь': '',
    #         'Э': 'E', 'э': 'e',
    #         'Ю': 'Yu', 'ю': 'yu',
    #         'Я': 'Ya', 'я': 'ya',
    #         'Ғ': 'Gʻ', 'ғ': 'gʻ',
    #         'Қ': 'Q', 'қ': 'q',
    #         'Ў': 'Oʻ', 'ў': 'oʻ',
    #         'Ҳ': 'H', 'ҳ': 'h',
    #     }
    #
    #     result = ''
    #     for char in text:
    #         result += mapping.get(char, char)
    #     return result

    @staticmethod
    def parse_russian_date(date_str):
        months = {
            "yanvar": "January", "fevral": "February", "mart": "March",
            "aprel": "April", "may": "May", "iyun": "June",
            "iyul": "July", "avgust": "August", "sentyabr": "September",
            "oktyabr": "October", "noyabr": "November", "dekabr": "December",
        }

        for ru, en in months.items():
            if ru in date_str:
                date_str = date_str.replace(ru, en)
                break

        parsed = dateparser.parse(date_str, languages=['uz', 'ru', 'en'])
        if parsed:
            published_at = parsed.strftime('%Y-%m-%d %H:%M:%S')
        else:
            published_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return published_at

    @staticmethod
    def fetch_html(url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                          "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Accept-Language": "uz-UZ,uz;q=0.9"
        }

        response = requests.get(url, headers=headers)
        time.sleep(5)
        return BeautifulSoup(response.text, 'html.parser')

    def get_all_news_url(self):
        post_url_set = set()
        for page_count in range(1, self.selectors['page_count'] + 1):
            page_bs = self.fetch_html(self.selectors['pagination_url'].format(page_count))
            print(self.selectors['pagination_url'].format(page_count))

            a_tag_list = page_bs.find_all('a')
            for a_tag in a_tag_list:
                # if self.selectors['base_url'] + a_tag.get('href') == src_last_data['url']:
                #     return post_url_set

                if self.selectors['is_url_required']:
                    post_url_set.add(self.selectors['base_url'] + a_tag.get('href'))
                else:
                    post_url_set.add(a_tag.get('href'))

        return post_url_set

    def parse_data(self, post_url_set):
        news_data_list = []
        for post_url in post_url_set:
            try:
                soup = self.fetch_html(post_url)
                post_data = self.selectors['post_data']

                if type(post_data['title']) is dict:
                    title_key = next(iter(post_data['title']))
                    title = soup.find(title_key, attrs=post_data['title'][title_key]).get_text(strip=True)
                else:
                    title = soup.find(post_data['title']).get_text(strip=True)

                print("title", title)

                if type(post_data['content']) is dict:
                    content_key = next(iter(post_data['content']))
                    content = soup.find(content_key, attrs=post_data['content'][content_key]).get_text(strip=True)
                else:
                    content = soup.find(post_data['content']).get_text(strip=True)

                print("content", content)

                published_at = ""
                if post_data['published_at'] is not None:
                    print(f"{post_data['published_at'] = }")
                    if type(post_data['published_at']) is dict:
                        published_at_key = next(iter(post_data['published_at']))
                        published_at = soup.find(published_at_key,
                                                 post_data['published_at'][published_at_key]).get_text(strip=True)
                    else:
                        published_at = soup.find(post_data['published_at']).get_text(strip=True)
                    if post_data['date_format'] is not None:
                        published_at = eval(post_data['date_format'])

                published_at = self.parse_russian_date(published_at)

                print("published_at", published_at)

                image_url_data = []
                if post_data['image_url'] is not None:
                    if type(post_data['image_url']) is dict:
                        image_key = next(iter(post_data['image_url']))
                        # image_url_list = soup.find_all(image_key, post_data['image_url'][image_key])
                        # for image_url in image_url_list:
                        #     image_url_data.append(image_url.get("src"))
                        # print(soup.find(image_key, post_data['image_url'][image_key]))
                        image_url_data.append(soup.find(image_key, post_data['image_url'][image_key]).get("src"))
                    else:
                        # image_url_list = soup.find_all(post_data['image_url'])
                        # for image_url in image_url_list:
                        #     image_url_data.append(image_url.get("src"))
                        image_url_data.append(soup.find(post_data['image_url']).get("src"))

                print("image_url_data", image_url_data)

                reaction_count = None
                if post_data['reaction_count'] is not None:
                    if type(post_data['reaction_count']) is dict:
                        reaction_count_key = next(iter(post_data['reaction_count']))
                        reaction_count = soup.find(reaction_count_key,
                                                   post_data['reaction_count'][reaction_count_key]).get_text(strip=True)
                    else:
                        reaction_count = soup.find(post_data['reaction_count']).get_text(strip=True)
                print("reaction_count", reaction_count)

                view_count = None
                if post_data['view_count'] is not None:
                    if type(post_data['view_count']) is dict:
                        view_count_key = next(iter(post_data['view_count']))
                        view_count = soup.find(view_count_key,
                                               post_data['view_count'][view_count_key]).get_text(strip=True)
                    else:
                        view_count = soup.find(post_data['view_count']).get_text(strip=True)
                print("view_count", view_count)
                news_data_list.append(
                    {
                        "url": post_url,
                        "title": title,
                        "content": content,
                        "image_url": image_url_data,
                        "published_at": published_at,
                        "category": None,
                        "view_count": view_count,
                        "reaction_count": reaction_count
                    }
                )
            except Exception as e:
                print(e, post_url)

        return news_data_list


if __name__ == "__main__":
    ## view_count olish
    ## reaction_count olish
    parser_config_list = [
        # {
        #     "base_url": "https://general-svr.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://general-svr.com/novosti",
        #     "source": "general-svr.com",
        #     "type": "global",
        #     "logo": "https://general-svr.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "btn btn-default taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://24htoday.net",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://24htoday.net/novosti",
        #     "source": "24htoday.net",
        #     "type": "global",
        #     "logo": "https://24htoday.net/templates/wp/image/logo.png   ",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "btn btn-default taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://mediamonstrosity.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://mediamonstrosity.com/novosti",
        #     "source": "mediamonstrosity.com",
        #     "type": "global",
        #     "logo": "https://mediamonstrosity.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://p-zona.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://p-zona.com/novosti",
        #     "source": "p-zona.com",
        #     "type": "global",
        #     "logo": "https://p-zona.com/templates/wp/img/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://1ubd.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://1ubd.com/novosti",
        #     "source": "1ubd.com",
        #     "type": "global",
        #     "logo": "https://1ubd.com/templates/wp/images/logo.jpg",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://hornbloger.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://hornbloger.com/novosti",
        #     "source": "hornbloger.com",
        #     "type": "global",
        #     "logo": "https://hornbloger.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://insayder2.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://insayder2.com/news",
        #     "source": "insayder2.com",
        #     "type": "global",
        #     "logo": "https://insayder2.com/templates/wp/images/w_logo.png",
        #     "post_data": {
        #         "title": {"h2": {"class": "title"}},
        #         "published_at": {"ul": {"class": "tgbanner__content-meta list-wrap"}},
        #         "date_format": "published_at.split(' ')[-1]",
        #         "content": {"div": {"class": "blog-details-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://nahalnews.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://nahalnews.com/novosti",
        #     "source": "nahalnews.com",
        #     "type": "global",
        #     "logo": "https://nahalnews.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "btn btn-default taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://kz-expert.info",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://kz-expert.info",
        #     "source": "kz-expert.info",
        #     "type": "global",
        #     "logo": "https://kz-expert.info/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"div": {"class": "blog-post-title"}},
        #         "published_at": {"div": {"class": "blog-post-time"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "blog-content pb-0"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://compro-r.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://compro-r.com",
        #     "source": "compro-r.com",
        #     "type": "global",
        #     "logo": None,
        #     "post_data": {
        #         "title": {"h1": {"class": "single_post_title_main"}},
        #         "published_at": {"span": {"class": "post-date updated"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "post_content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://falshivok.net",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://falshivok.net/novosti",
        #     "source": "falshivok.net",
        #     "type": "global",
        #     "logo": "https://falshivok.net/templates/wp/img/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": None,
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://7-club-7.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://7-club-7.com/novosti",
        #     "source": "7-club-7.com",
        #     "type": "global",
        #     "logo": "https://7-club-7.com/templates/wp/img/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://tlvinsider.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://tlvinsider.com/novosti",
        #     "source": "tlvinsider.com",
        #     "type": "global",
        #     "logo": "https://tlvinsider.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle post_title"}},
        #         "published_at": {"small": {"class": "pull-left"}},
        #         "date_format": "published_at.split(': ')[-1]",
        #         "content": {"div": {"class": "itemFullText"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://sitetalkzone.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://sitetalkzone.com/novosti",
        #     "source": "sitetalkzone.com",
        #     "type": "global",
        #     "logo": "https://sitetalkzone.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": None,
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "http://ru-smi.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "http://ru-smi.com",
        #     "source": "ru-smi.com",
        #     "type": "global",
        #     "logo": "https://ru-smi.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": None,
        #         "date_format": None,
        #         "content": {"div": {"class": "content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://compromat41.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://compromat41.com/novosti",
        #     "source": "compromat41.com",
        #     "type": "global",
        #     "logo": "https://compromat41.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"span": {"class": "itemDateCreated"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://v-kurse2.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://v-kurse2.com",
        #     "source": "v-kurse2.com",
        #     "type": "global",
        #     "logo": "https://v-kurse2.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "main-title"}},
        #         "published_at": {"span": {"class": "text"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://historyofcoins.org",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://historyofcoins.org",
        #     "source": "historyofcoins.org",
        #     "type": "global",
        #     "logo": None,
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "http://internetproekt.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "http://internetproekt.com",
        #     "source": "internetproekt.com",
        #     "type": "global",
        #     "logo": "http://internetproekt.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"span": {"class": "itemDateCreated"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "item-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://kontent24.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://kontent24.com",
        #     "source": "kontent24.com",
        #     "type": "global",
        #     "logo": "https://kontent24.com/templates/wp/assets/img/logo-1.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": None,
        #         "date_format": None,
        #         "content": {"div": {"class": "article-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://futlyar.net",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://futlyar.net",
        #     "source": "futlyar.net",
        #     "type": "global",
        #     "logo": "https://futlyar.net/templates/wp/img/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://blogs-exposed.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://blogs-exposed.com",
        #     "source": "blogs-exposed.com",
        #     "type": "global",
        #     "logo": None,
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": None,
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://balansst.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://balansst.com",
        #     "source": "balansst.com",
        #     "type": "global",
        #     "logo": "https://balansst.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "btn btn-default taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "http://katarsis7.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "http://katarsis7.com",
        #     "source": "katarsis7.com",
        #     "type": "global",
        #     "logo": "https://katarsis7.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"div": {"class": "blog-post-title"}},
        #         "published_at": {"div": {"class": "post-date-author"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "article-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://tv-lenta.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://tv-lenta.com",
        #     "source": "tv-lenta.com",
        #     "type": "global",
        #     "logo": "https://tv-lenta.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://informanet.org",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://informanet.org",
        #     "source": "informanet.org",
        #     "type": "global",
        #     "logo": "https://informanet.org/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://p-efir.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://p-efir.com",
        #     "source": "p-efir.com",
        #     "type": "global",
        #     "logo": "https://p-efir.com/templates/wp/images/logo-light.png",
        #     "post_data": {
        #         "title": {"div": {"class": "blog-post-title"}},
        #         "published_at": {"div": {"class": "blog-post-time"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "blog-content pb-0"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://fayrix.org",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://fayrix.org",
        #     "source": "fayrix.org",
        #     "type": "global",
        #     "logo": None,
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": None,
        #         "date_format": None,
        #         "content": {"div": {"class": "item-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://refinancesandiego.org",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://refinancesandiego.org",
        #     "source": "refinancesandiego.org",
        #     "type": "global",
        #     "logo": "https://refinancesandiego.org/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "http://premiumpixel.net",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "http://premiumpixel.net",
        #     "source": "premiumpixel.net",
        #     "type": "global",
        #     "logo": "https://refinancesandiego.org/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "btn btn-default taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://can-explain.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://can-explain.com",
        #     "source": "can-explain.com",
        #     "type": "global",
        #     "logo": "https://can-explain.com/templates/wp/assets/images/logo.png",
        #     "post_data": {
        #         "title": {"h3": {"class": "entry-title"}},
        #         "published_at": {"div": {"class": "entry-date"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://politica2.info",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://politica2.info",
        #     "source": "politica2.info",
        #     "type": "global",
        #     "logo": "https://politica2.info/templates/wp/images/logo_sticky.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": None,
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://chatname.net",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://chatname.net",
        #     "source": "chatname.net",
        #     "type": "global",
        #     "logo": "https://chatname.net/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://dvsslco24.org",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://dvsslco24.org",
        #     "source": "dvsslco24.org",
        #     "type": "global",
        #     "logo": "https://dvsslco24.org/templates/wp/image/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": {"a": {"class": "btn btn-default taga"}},
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },
        # {
        #     "base_url": "https://persona-l.com",
        #     "is_url_required": True,
        #     "page_count": 1,
        #     "pagination_url": "https://persona-l.com",
        #     "source": "persona-l.com",
        #     "type": "global",
        #     "logo": "https://persona-l.com/templates/wp/images/logo.png",
        #     "post_data": {
        #         "title": {"h1": {"class": "itemTitle"}},
        #         "published_at": None,
        #         "date_format": None,
        #         "content": {"div": {"class": "entry-content"}},
        #         "category": None,
        #         "view_count": None,
        #         "reaction_count": None,
        #         "image_url": None
        #     }
        # },

    ]

    for parser_config in parser_config_list:
        new_parser = NewsParser("https://www.ozodlik.org",
                                parser_config
                                )

        # last_data = get_last_news(parser_config['source'])
        # url_set = new_parser.get_all_news_url()
        # print(url_set)
        # post_data_list = new_parser.parse_data(url_set)

        post_data_list = new_parser.parse_data(
            [
                "https://www.norma.uz/oz/qonunchilikda_yangi/pedagog_kadrlarni_tayerlashda_sirtqi_talimdan_voz_kechiladi"])

        final_data = {
            "source": parser_config['source'],
            "type": parser_config['type'],
            "logo": parser_config['logo'],
            "posts": post_data_list,
        }
        # print(final_data)
        new_parser.save_to_json(final_data, parser_config['source'] + ".json")
        # send_data(final_data)
