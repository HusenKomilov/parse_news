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
                # print(soup)
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
        {
            "base_url": "https://timesofindia.indiatimes.com",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://timesofindia.indiatimes.com",
            "source": "timesofindia.indiatimes.com",
            "type": "global",
            "logo": None,
            "post_data": {
                "title": {"h1": {"class": "HNMDR"}},
                "published_at": None,
                "date_format": None,
                "content": {"div": {"class": "fewcent-121230839 js_tbl_article"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://wan-ifra.org",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://wan-ifra.org/news/page/{}",
            "source": "wan-ifra.org",
            "type": "global",
            "logo": "https://wan-ifra.org/wp-content/themes/wan-ifra/images/logo.png",
            "post_data": {
                "title": "main",
                "published_at": None,
                "date_format": None,
                "content": {"div": {"class": "text"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://kizzyklicks.blogspot.com",
            "is_url_required": True,
            "page_count": 1,
            "pagination_url": "https://kizzyklicks.blogspot.com",
            "source": "kizzyklicks.blogspot.com",
            "type": "global",
            "logo": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0bPZVoqWT43xFqG67jd5lWpGE2kBQ8-s_wyRuPkstHX0jCiUpU-7fJqGRKTPEPVUpLoxTNc5vBUJMhCOSk27rvWSgRK96XheGCYRjvGNJ3ITWyAz8bN98lXdLS-sbWXlT9Wtq8soJ1ztg/s1600/KIZZYKLICKS+NEW.png",
            "post_data": {
                "title": {"h1": {"class": "post-title"}},
                "published_at": {"span": {"class": "post-date published"}},
                "date_format": None,
                "content": {"div": {"class": "post-body post-content"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://reporter.am",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://reporter.am",
            "source": "reporter.am",
            "type": "global",
            "logo": "https://reporter.am/wp-content/uploads/2022/07/am-reporter-2.png",
            "post_data": {
                "title": {"h1": {"class": "page-title"}},
                "published_at": {"span": {"itemprop": "datePublished dateModified"}},
                "date_format": None,
                "content": {"div": {"class": "entry"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://internewscast.com",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://internewscast.com",
            "source": "internewscast.com",
            "type": "global",
            "logo": "https://internewscast.com/wp-content/uploads/2025/04/INTERNEWSCAST-icon-1.png",
            "post_data": {
                "title": {"h1": {"class": "entry-title"}},
                "published_at": {"time": {"class": "entry-date published"}},
                "date_format": None,
                "content": {"div": {"class": "entry-content"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.npr.org",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://www.npr.org/sections/news/",
            "source": "npr.org",
            "type": "global",
            "logo": "https://static-assets.npr.org/chrome_svg/npr-logo-2025.svg",
            "post_data": {
                "title": {"div": {"class": "storytitle"}},
                "published_at": {"span": {"class": "date"}},
                "date_format": None,
                "content": {"div": {"class": "storytext storylocation linkLocation"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.watchdoguganda.com",
            "is_url_required": False,
            "page_count": 3,
            "pagination_url": "https://www.watchdoguganda.com/category/news/page/{}",
            "source": "watchdoguganda.com",
            "type": "global",
            "logo": "https://www.watchdoguganda.com/wp-content/uploads/2019/01/logo-1-1-1.png",
            "post_data": {
                "title": {"h1": {"class": "jeg_post_title"}},
                "published_at": {"div": {"class": "jeg_meta_date"}},
                "date_format": None,
                "content": {"div": {"class": "content-inner"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://africalaunchpad.com",
            "is_url_required": False,
            "page_count": 3,
            "pagination_url": "https://africalaunchpad.com/news/page/{}",
            "source": "africalaunchpad.com",
            "type": "global",
            "logo": "https://africalaunchpad.com/wp-content/uploads/2022/12/africa-launch-pad-logo249x85.webp",
            "post_data": {
                "title": {"h1": {"class": "entry-title"}},
                "published_at": {"p": {"class": "post-modified-info"}},
                "date_format": None,
                "content": {"div": {"class": "entry-content"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://worldcelebritynews.com",
            "is_url_required": False,
            "page_count": 3,
            "pagination_url": "https://worldcelebritynews.com/category-list?page={}",
            "source": "worldcelebritynews.com",
            "type": "global",
            "logo": "https://worldcelebritynews.com/storage/img-9672-removebg-preview-2.png",
            "post_data": {
                "title": {"h1": {"class": "post-title"}},
                "published_at": {"span": {"class": "post-on has-dot"}},
                "date_format": None,
                "content": {"div": {"class": "ck-content"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.latimes.com",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://www.latimes.com",
            "source": "latimes.com",
            "type": "global",
            "logo": None,
            "post_data": {
                "title": {"h1": {"class": "headline"}},
                "published_at": {"span": {"class": "published-date-day"}},
                "date_format": None,
                "content": {"div": {"class": "ct-rich-text-children font-cmsFontBrandText font-normal text-lg leading-7.75 [&_>p]:text-cms-story-body-color-text clearfix mb-10 md:max-w-170 md:mx-auto"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://quintdaily.com",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://quintdaily.com",
            "source": "quintdaily.com",
            "type": "global",
            "logo": "https://quintdaily.com/wp-content/uploads/2021/06/Quintdaily-Logo-1.png",
            "post_data": {
                "title": {"h1": {"class": "entry-title"}},
                "published_at": {"span": {"class": "td-post-date"}},
                "date_format": None,
                "content": {"div": {"class": "td-post-content"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.theunionjournal.com",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://www.theunionjournal.com",
            "source": "theunionjournal.com",
            "type": "global",
            "logo": "https://cdn.shortpixel.ai/spai/q_lossy+w_150+to_auto+ret_img/www.theunionjournal.com/wp-content/uploads/2020/11/test-logo-4-150x150-1.png",
            "post_data": {
                "title": {"h1": {"class": "entry-title"}},
                "published_at": {"time": {"class": "entry-date updated td-module-date"}},
                "date_format": None,
                "content": {"div": {"class": "markdown prose w-full break-words dark:prose-invert dark"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.dainikviral.com",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://www.dainikviral.com",
            "source": "dainikviral.com",
            "type": "global",
            "logo": "https://www.dainikviral.com/wp-content/uploads/2023/08/cropped-cropped-cropped-cropped-cropped-Dainik-Viral-Picture-1.png",
            "post_data": {
                "title": {"h1": {"class": "entry-title"}},
                "published_at": {"time": {"class": "entry-date published"}},
                "date_format": None,
                "content": {"div": {"class": "entry-content"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://bbcbreakingnews.com",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://bbcbreakingnews.com",
            "source": "bbcbreakingnews.com",
            "type": "global",
            "logo": None,
            "post_data": {
                "title": {"h1": {"class": "title"}},
                "published_at": None,
                "date_format": None,
                "content": {"article": {"class": "small single"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.worldpresslive.com",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://www.worldpresslive.com",
            "source": "worldpresslive.com",
            "type": "global",
            "logo": "https://www.worldpresslive.com/wp-content/uploads/2022/06/WORD-PRESS-LIVE-01.png",
            "post_data": {
                "title": {"h1": {"class": "post-title single-post-title entry-title"}},
                "published_at": {"time": {"class": "entry-date published"}},
                "date_format": None,
                "content": {"div": {"class": "inner-post-entry entry-content"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.akinblog.com",
            "is_url_required": False,
            "page_count": 3,
            "pagination_url": "https://www.akinblog.com/page/{}",
            "source": "akinblog.com",
            "type": "global",
            "logo": None,
            "post_data": {
                "title": {"h1": {"class": "title single"}},
                "published_at": {"span": {"class": "mg-blog-date"}},
                "date_format": None,
                "content": {"article": {"class": "page-content-single small single"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
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
                "https://www.akinblog.com/davido-the-journey-of-an-afrobeats-icon/"])

        final_data = {
            "source": parser_config['source'],
            "type": parser_config['type'],
            "logo": parser_config['logo'],
            "posts": post_data_list,
        }
        # print(final_data)
        new_parser.save_to_json(final_data, parser_config['source'] + ".json")
        # send_data(final_data)
