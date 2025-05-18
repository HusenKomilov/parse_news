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
            "base_url": "https://www.bbc.com",
            "is_url_required": True,
            "page_count": 1,
            "pagination_url": "https://www.bbc.com",
            "source": "bbc.com",
            "type": "global",
            "logo": None,
            "post_data": {
                "title": {"h1": {"class": "sc-f98b1ad2-0 dfvxux"}},
                "published_at": {"time": {"class": "sc-801dd632-2 IvNnh"}},
                "date_format": None,
                "content": {"div": {"data-component": "text-block"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://syrianwar1.blogspot.com",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://syrianwar1.blogspot.com",
            "source": "syrianwar1.blogspot.com",
            "type": "global",
            "logo": None,
            "post_data": {
                "title": {"h3": {"class": "post-title entry-title"}},
                "published_at": {"h2": {"class": "date-header"}},
                "date_format": None,
                "content": {"div": {"class": "post-body entry-content"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://edition.cnn.com",
            "is_url_required": True,
            "page_count": 1,
            "pagination_url": "https://edition.cnn.com",
            "source": "edition.cnn.com",
            "type": "global",
            "logo": None,
            "post_data": {
                "title": {"h1": {"class": "headline__text inline-placeholder vossi-headline-text"}},
                "published_at": {"div": {"class": "timestamp vossi-timestamp"}},
                "date_format": None,
                "content": {"div": {"class": "article__content"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://rhymes-punches.com",
            "is_url_required": True,
            "page_count": 1,
            "pagination_url": "https://rhymes-punches.com",
            "source": "rhymes-punches.com",
            "type": "global",
            "logo": "https://rhymes-punches.com/templates/wp/img/logo.png",
            "post_data": {
                "title": {"div": {"class": "blog-post-title"}},
                "published_at": {"div": {"class": "post-date-author"}},
                "date_format": None,
                "content": {"div": {"class": "article-content"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://asiaplustj.info",
            "is_url_required": True,
            "page_count": 3,
            "pagination_url": "https://asiaplustj.info/ru/news/all?page={}",
            "source": "asiaplustj.info",
            "type": "global",
            "logo": "https://asiaplustj.info/sites/all/themes/asiaplus/images/logo-front.png?v4",
            "post_data": {
                "title": {"h1": {"class": "atitle"}},
                "published_at": {"div": {"class": "article-info"}},
                "date_format": None,
                "content": {"div": {"class": "article-body js-mediator-article"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://astanatv.kz",
            "is_url_required": True,
            "page_count": 3,
            "pagination_url": "https://astanatv.kz/kz/news/?page={}",
            "source": "astanatv.kz",
            "type": "global",
            "logo": "https://astanatv.kz/assets/astanatv-logo.png",
            "post_data": {
                "title": {"h1": {"class": "news__title xl-mb-20 xs-mb-20"}},
                "published_at": {"div": {"class": "news__date xl-mr-20"}},
                "date_format": None,
                "content": {"div": {"class": "news-full-text"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://kazpravda.kz",
            "is_url_required": True,
            "page_count": 1,
            "pagination_url": "https://kazpravda.kz",
            "source": "kazpravda.kz",
            "type": "global",
            "logo": None,
            "post_data": {
                "title": {"h1": {"class": "article__title"}},
                "published_at": {"time": {"class": "article__date"}},
                "date_format": None,
                "content": {"div": {"class": "article__body"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://iz.ru",
            "is_url_required": True,
            "page_count": 1,
            "pagination_url": "https://iz.ru/news",
            "source": "iz.ru",
            "type": "global",
            "logo": None,
            "post_data": {
                "title": {"h1": {"itemprop": "headline"}},
                "published_at": {"div": {"class": "article_page__left__top__time__label"}},
                "date_format": None,
                "content": {"div": {"itemprop": "articleBody"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.trend.az",
            "is_url_required": False,
            "page_count": 1,
            "pagination_url": "https://www.trend.az/latest/",
            "source": "trend.az",
            "type": "global",
            "logo": "https://www.trend.az/assets/img/logo30.svg?v558",
            "post_data": {
                "title": {"div": {"class": "top-part"}},
                "published_at": {"span": {"class": "date-time"}},
                "date_format": None,
                "content": {"div": {"itemprop": "articleBody"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.ozodlik.org",
            "is_url_required": True,
            "page_count": 3,
            "pagination_url": "https://www.ozodlik.org/z/421?p={}",
            "source": "ozodlik.org",
            "type": "global",
            "logo": "72a38011d72261932735c12480557d8274d34635e2c28eee2ab1f58ab0f3b39a.png",
            "post_data": {
                "title": {"h1": {"class": "title pg-title"}},
                "published_at": {"span": {"class": "date"}},
                "date_format": None,
                "content": {"div": {"id": "article-content"}},
                "category": None,
                "view_count": None,
                "reaction_count": {"span": {"class": "meta-item post-views has-icon rank-hot"}},
                "image_url": "img"
            }
        },
        {
            "base_url": "https://www.newsru.com",
            "is_url_required": True,
            "page_count": 1,
            "pagination_url": "https://www.newsru.com/allnews",
            "source": "newsru.com",
            "type": "global",
            "logo": "https://static.newsru.com/static/v3/img/misc/rucom_main.png",
            "post_data": {
                "title": {"h1": {"class": "article-title"}},
                "published_at": {"div": {"class": "article-date"}},
                "date_format": None,
                "content": {"div": {"class": "article-text"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://niann.ru",
            "is_url_required": True,
            "page_count": 1,
            "pagination_url": "https://niann.ru",
            "source": "niann.ru",
            "type": "global",
            "logo": "https://niann.ru/_data/objects/0000/0170/icon.png",
            "post_data": {
                "title": {"h1": {"class": "header"}},
                "published_at": {"span": {"class": "date_standart date"}},
                "date_format": None,
                "content": {"div": {"class": "mess_standart"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.chechnyafree.ru",
            "is_url_required": False,
            "page_count": 3,
            "pagination_url": "https://www.chechnyafree.ru/page/{}",
            "source": "chechnyafree.ru",
            "type": "global",
            "logo": None,
            "post_data": {
                "title": {"h1": {"class": "entry-title"}},
                "published_at": {"time": {"class": "entry-date published updated"}},
                "date_format": None,
                "content": {"div": {"class": "entry-content clearfix"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://24.kg",
            "is_url_required": True,
            "page_count": 3,
            "pagination_url": "https://24.kg/page_{}",
            "source": "24.kg",
            "type": "global",
            "logo": "https://24.kg/assets/7a772a43/images/logo.png",
            "post_data": {
                "title": {"h1": {"class": "newsTitle"}},
                "published_at": {"span": {"itemprop": "datePublished"}},
                "date_format": None,
                "content": {"div": {"class": "cont"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.inopressa.ru",
            "is_url_required": True,
            "page_count": 1,
            "pagination_url": "https://www.inopressa.ru",
            "source": "inopressa.ru",
            "type": "global",
            "logo": "https://static.inopressa.ru/img/inopressa-logo-light.gif",
            "post_data": {
                "title": {"div": {"class": "topic"}},
                "published_at": {"div": {"class": "maincaption"}},
                "date_format": None,
                "content": {"div": {"class": "body"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.ntv.ru",
            "is_url_required": True,
            "page_count": 3,
            "pagination_url": "https://www.ntv.ru/novosti?page={}",
            "source": "ntv.ru",
            "type": "global",
            "logo": "https://static2.ntv.ru/static/images/logo.png",
            "post_data": {
                "title": {"h1": {"class": "h h-l content-top__title"}},
                "published_at": {"p": {"class": "cap cap-xs content-top__date"}},
                "date_format": None,
                "content": {"div": {"class": "content-text"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://www.rosbalt.ru",
            "is_url_required": True,
            "page_count": 1,
            "pagination_url": "https://www.rosbalt.ru/news",
            "source": "rosbalt.ru",
            "type": "global",
            "logo": "https://files.1mi.media/39de3f037a203dee014c6bddc7d37b5804aacd91/resize:auto:0:0:0/c41a92fe9ea4f6991bbf9950fe6fa3fa53e9bfd31ef1bef46d9b59f9398a.svg",
            "post_data": {
                "title": {"h1": {"class": "MatterTopNoImage_title___N52h"}},
                "published_at": {"div": {"class": "MatterTopNoImage_date__u0xOz"}},
                "date_format": None,
                "content": {"div": {"class": "mb-[24px] lg:mb-[36px] content-blocks kind-common"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://alisnad.com",
            "is_url_required": False,
            "page_count": 3,
            "pagination_url": "https://alisnad.com/page/{}",
            "source": "alisnad.com",
            "type": "global",
            "logo": "https://alisnad.com/wp-content/uploads/2020/01/Logo-no-com-300x98.png",
            "post_data": {
                "title": {"h1": {"class": "entry-title"}},
                "published_at": {"time": {"class": "entry-date updated td-module-date"}},
                "date_format": None,
                "content": {"div": {"class": "td-post-content"}},
                "category": None,
                "view_count": None,
                "reaction_count": None,
                "image_url": None
            }
        },
        {
            "base_url": "https://vasudeva.ru",
            "is_url_required": True,
            "page_count": 1,
            "pagination_url": "https://vasudeva.ru",
            "source": "vasudeva.ru",
            "type": "global",
            "logo": "https://vasudeva.ru/images/logo251.jpg",
            "post_data": {
                "title": {"h1": {"itemprop": "headline"}},
                "published_at": {"time": {"itemprop": "datePublished"}},
                "date_format": None,
                "content": {"div": {"itemprop": "articleBody"}},
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
                "https://vasudeva.ru/universitet-bkhakti-jogi/dukhovnye-uchitelya/shrila-prabhupada/o-shrile-prabkhupade/baradradzha-das-luchshaya-nagrada"])

        final_data = {
            "source": parser_config['source'],
            "type": parser_config['type'],
            "logo": parser_config['logo'],
            "posts": post_data_list,
        }
        # print(final_data)
        new_parser.save_to_json(final_data, parser_config['source'] + ".json")
        # send_data(final_data)
