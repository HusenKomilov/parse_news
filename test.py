parser_config_list = [
    {
        "base_url": "https://daryo.uz",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://daryo.uz/yangiliklar",
        "source": "daryo.uz",
        "type": "local",
        "logo": "https://daryo.uz/logo/logo-white.svg",
        "post_data": {
            "title": {"h1": {"class": "is-title post-title post-view-title"}},
            "published_at": {"time": {"class": "post-date"}},
            "date_format": None,
            "content": {"div": {"class": "post-content-wrap has-share-float"}},
            "category": None,
            "view_count": None,
            "reaction_count": {"span": {"class": "meta-item post-views has-icon rank-hot"}},
            "image_url": None
        }
    },
    {
        "base_url": "https://kun.uz",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://kun.uz/news/list",
        "source": "kun.uz",
        "type": "local",
        "logo": "4ea914010683e95be91a8074048b3e971c53f30085d454002cd8d0b077b91099.png",
        "post_data": {
            "title": {"h1": {"class": "news-inner__content-title"}},
            "published_at": {"div": {"class": "news-inner__content-stats"}},
            "date_format": "published_at.split('|')[-1].replace('/','')",
            "content": {"div": {"class": "news-inner__content-page"}},
            "category": None,
            "view_count": None,
            "reaction_count": {"span": {"class": "meta-item post-views has-icon rank-hot"}},
            "image_url": "img"
        }
    },
    {
        "base_url": "https://www.gazeta.uz",
        "is_url_required": True,
        "page_count": 5,
        "pagination_url": "https://www.gazeta.uz/oz/list/news?page={}",
        "source": "gazeta.uz",
        "type": "local",
        "logo": "https://www.gazeta.uz/i/gazeta_logo.svg",
        "post_data": {
            "title": {"h1": {"itemprop": "headline name"}},
            "published_at": {"div": {"class": "articleDateTime"}},
            "date_format": None,
            "content": {"div": {"class": "js-mediator-article article-text"}},
            "category": {"span": {"itemprop": "name"}},
            "view_count": None,
            "reaction_count": None,
            "image_url": {"img": {"class": "articleBigPic"}}
        }
    },
    {
        "base_url": "https://xabar.uz",
        "is_url_required": False,
        "page_count": 1,
        "pagination_url": "https://xabar.uz/yangiliklar",
        "source": "xabar.uz",
        "type": "local",
        "logo": "https://xabar.uz/static/assets/73a7d9c9/img/logo-desktop.svg",
        "post_data": {
            "title": {"h2": {"class": "post__title"}},
            "published_at": {"span": {"class": "date-time"}},
            "date_format": None,
            "content": {"div": {"class": "post__body"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": {"div": {"class": "media"}}
        }
    },
    {
        "base_url": "https://qalampir.uz/uz",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://qalampir.uz/uz/latest",
        "source": "qalampir.uz",
        "type": "local",
        "logo": None,
        "post_data": {
            "title": {"h1": {"class": "text"}},
            "published_at": None,
            "date_format": None,
            "content": {"div": {"class": "row g-4 my-main-content"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": {"img": {"class": "mainImg"}}
        }
    },
    {
        "base_url": "https://batafsil.uz",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://batafsil.uz/all_news",
        "source": "batafsil.uz",
        "type": "local",
        "logo": "https://batafsil.uz/bitrix/templates/main_2020/images/logo_uz.png",
        "post_data": {
            "title": {"h1": {"class": "post-title entry-title"}},
            "published_at": {"time": {"class": "entry-date published updated"}},
            "date_format": None,
            "content": {"div": {"class": "detail-text"}},
            "category": {"span": {"class": "cat-title"}},
            "view_count": {"div": {"class": "post-read-time"}},
            "reaction_count": None,
            "image_url": {"img": {"class": "attachment-inhype-blog-thumb size-inhype-blog-thumb wp-post-image"}}
        }
    },
    {
        "base_url": "https://uza.uz/uz",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://uza.uz/uz/posts",
        "source": "uza.uz",
        "type": "local",
        "logo": "https://uza.uz/static/media/uza-logo.c5b4dfd5.svg",
        "post_data": {
            "title": {"div": {"class": "news-top-head__title"}},
            "published_at": {"div": {"class": "news-top-head__date"}},
            "date_format": "published_at.split('|')[-1].replace('/','')",
            "content": {"div": {"class": "content-block"}},
            "category": {"div": {"class": "news-top-head__meta"}},
            "view_count": None,
            "reaction_count": None,
            "image_url": {"img": {"class": "news-top-head__img"}}
        }
    },
    {
        "base_url": "https://sputniknews.uz",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://sputniknews.uz/news",
        "source": "sputniknews.uz",
        "type": "local",
        "logo": None,
        "post_data": {
            "title": {"h1": {"class": "article__title"}},
            "published_at": {"div": {"class": "article__info-date"}},
            "date_format": None,
            "content": {"div": {"class": "article__body"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://anhor.uz/uzl",
        "is_url_required": False,
        "page_count": 1,
        "pagination_url": "https://anhor.uz/uzl",
        "source": "anhor.uz",
        "type": "local",
        "logo": "https://anhor.uz/wp-content/themes/anhor/assets/img/logo.png",
        "post_data": {
            "title": {"h1": {"class": "article__head"}},
            "published_at": {"span": {"class": "posts-list__date post-meta__item post-meta__date"}},
            "date_format": None,
            "content": {"div": {"class": "article__content"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": {"img": {"class": "article__img wp-post-image"}}
        }
    },
    {
        "base_url": "https://www.norma.uz/oz",
        "is_url_required": True,
        "page_count": 3,
        "pagination_url": "https://www.norma.uz/oz/?page={}&limit=28",
        "source": "norma.uz",
        "type": "local",
        "logo": "https://www.norma.uz/files/norma.uz/images/logo.png",
        "post_data": {
            "title": {"h1": {"class": "pos_0"}},
            "published_at": {"p": {"class": "date"}},
            "date_format": None,
            "content": {"div": {"class": "fullText"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://repost.uz/uz",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://repost.uz/uz",
        "source": "repost.uz",
        "type": "local",
        "logo": None,
        "post_data": {
            "title": {"h1": {"itemprop": "headline"}},
            "published_at": None,
            "date_format": None,
            "content": {"div": {"class": "article__content"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://upl.uz",
        "is_url_required": False,
        "page_count": 1,
        "pagination_url": "https://upl.uz",
        "source": "upl.uz",
        "type": "local",
        "logo": None,
        "post_data": {
            "title": {"h1": {"class": "post-title"}},
            "published_at": {"span": {"itemprop": "datePublished"}},
            "date_format": None,
            "content": {"div": {"itemprop": "articleBody"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://uznews.uz/uz",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://uznews.uz/uz/news",
        "source": "uznews.uz",
        "type": "local",
        "logo": "https://uznews.uz/assets/img/logo.svg",
        "post_data": {
            "title": {"h1": {"class": "section-header-title title title--m"}},
            "published_at": {"span": {"class": "section-header-date"}},
            "date_format": None,
            "content": {"div": {"class": "content"}},
            "category": None,
            "view_count": {"span": {"class": "widgets-item-text"}},
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://rg.ru",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://rg.ru/news.html",
        "source": "rg.ru",
        "type": "global",
        "logo": None,
        "post_data": {
            "title": {"h1": {"class": "PageArticleCommonTitle_title__fUDQW"}},
            "published_at": {"div": {"class": "ContentMetaDefault_date__wS0te"}},
            "date_format": None,
            "content": {"div": {
                "class": "PageContentCommonStyling_text__CKOzO commonArticle_text__ul5uZ commonArticle_zoom__SDMjc"}},
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
            "title": {"h1": {"class": "m-t-10"}},
            "published_at": {"div": {"class": "article_page__left__top__time__label"}},
            "date_format": None,
            "content": {"div": {
                "itemprop": "articleBody"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://www.kp.ru",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://www.kp.ru/online",
        "source": "kp.ru",
        "type": "global",
        "logo": None,
        "post_data": {
            "title": {"h1": {"class": "sc-j7em19-3 eyeguj"}},
            "published_at": {"span": {"class": "sc-j7em19-1 dtkLMY"}},
            "date_format": None,
            "content": {"div": {
                "class": "sc-1wayp1z-0 sc-1wayp1z-5 gwmrBl chEeRL"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": {"img": {"class": "sc-foxktb-1 cYprnQ"}}
        }
    },
    {
        "base_url": "https://aif.ru",
        "is_url_required": False,
        "page_count": 1,
        "pagination_url": "https://aif.ru/news",
        "source": "aif.ru",
        "type": "global",
        "logo": "https://aif.ru/redesign2018/img/logo.svg?14a",
        "post_data": {
            "title": {"h1": {"itemprop": "headline"}},
            "published_at": {"time": {"itemprop": "datePublished"}},
            "date_format": None,
            "content": {"div": {
                "class": "article_text"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": {"img": {"itemprop": "image"}}
        }
    },
    {
        "base_url": "https://sputnikglobe.com",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://sputnikglobe.com/news",
        "source": "sputnikglobe.com",
        "type": "global",
        "logo": None,
        "post_data": {
            "title": {"h1": {"class": "article__title"}},
            "published_at": {"div": {"class": "article__info-date"}},
            "date_format": None,
            "content": {"div": {"class": "article__body"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://www.rt.com",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://www.rt.com",
        "source": "rt.com",
        "type": "global",
        "logo": None,
        "post_data": {
            "title": {"h1": {"class": "article__heading"}},
            "published_at": {"span": {"class": "date date_article-header"}},
            "date_format": None,
            "content": {"div": {"class": "article__text text"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://ria.ru",
        "is_url_required": False,
        "page_count": 1,
        "pagination_url": "https://ria.ru",
        "source": "ria.ru",
        "type": "global",
        "logo": None,
        "post_data": {
            "title": {"div": {"class": "article__title"}},
            "published_at": {"div": {"class": "article__info-date"}},
            "date_format": None,
            "content": {"div": {"class": "article__body js-mediator-article mia-analytics"}},
            "category": None,
            "view_count": {"span": {"class": "article__views"}},
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://www.kommersant.ru",
        "is_url_required": True,
        "page_count": 3,
        "pagination_url": "https://www.kommersant.ru/lenta?from=all_lenta&page={}",
        "source": "kommersant.ru",
        "type": "global",
        "logo": None,
        "post_data": {
            "title": {"h1": {"class": "doc_header__name js-search-mark"}},
            "published_at": {"time": {"class": "doc_header__publish_time"}},
            "date_format": None,
            "content": {"div": {"class": "article_text_wrapper js-search-mark"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://www.vedomosti.ru",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://www.vedomosti.ru",
        "source": "vedomosti.ru",
        "type": "global",
        "logo": None,
        "post_data": {
            "title": {"h1": {"class": "article-headline__title"}},
            "published_at": {"time": {"class": "article-meta__date"}},
            "date_format": None,
            "content": {"div": {"class": "article-boxes-list article__boxes"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://www.gazeta.ru",
        "is_url_required": True,
        "page_count": 3,
        "pagination_url": "https://www.gazeta.ru/news/?p=main&d=1747317476&page={}",
        "source": "gazeta.ru",
        "type": "global",
        "logo": "https://static.gazeta.ru/nm2021/img/logo_2021.svg",
        "post_data": {
            "title": {"h1": {"class": "headline"}},
            "published_at": {"time": {"itemprop": "datePublished"}},
            "date_format": None,
            "content": {"div": {"class": "b_article-text"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": {"img": {"class": "item-image"}}
        }
    },
    {
        "base_url": "https://www.mk.ru",
        "is_url_required": False,
        "page_count": 3,
        "pagination_url": "https://www.mk.ru/news/{}/",
        "source": "mk.ru",
        "type": "global",
        "logo": "https://www.mk.ru/media/mkru2020/img/mk-logo.svg",
        "post_data": {
            "title": {"h1": {"class": "article__title"}},
            "published_at": {"time": {"class": "meta__text"}},
            "date_format": None,
            "content": {"div": {"class": "article__body"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": {"img": {"class": "article__picture-image"}}
        }
    },
    {
        "base_url": "https://www.themoscowtimes.com",
        "is_url_required": False,
        "page_count": 1,
        "pagination_url": "https://www.themoscowtimes.com/news",
        "source": "themoscowtimes.com",
        "type": "global",
        "logo": "https://static.themoscowtimes.com/img/logo_tmt_30_yo.svg",
        "post_data": {
            "title": {"header": {"class": "article__header"}},
            "published_at": {"time": {"class": "byline__datetime timeago"}},
            "date_format": None,
            "content": {"div": {"class": "article__block article__block--html article__block--column"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://meduza.io",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://meduza.io",
        "source": "meduza.io",
        "type": "global",
        "logo": None,
        "post_data": {
            "title": {"h1": {"class": "RichTitle-module_root__U5XQu"}},
            "published_at": {"time": {"class": "Timestamp-module_root__jPJ6w"}},
            "date_format": None,
            "content": {"div": {"class": "GeneralMaterial-module-article"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://www.inform.kz",
        "is_url_required": True,
        "page_count": 3,
        "pagination_url": "https://www.inform.kz/lenta/?page={}",
        "source": "inform.kz",
        "type": "global",
        "logo": None,
        "post_data": {
            "title": {"h1": {"class": "article__title"}},
            "published_at": {"div": {"class": "article__time"}},
            "date_format": None,
            "content": {"div": {"class": "article__body-text"}},
            "category": None,
            "view_count": None,
            "reaction_count": None,
            "image_url": None
        }
    },
    {
        "base_url": "https://egemen.kz",
        "is_url_required": True,
        "page_count": 3,
        "pagination_url": "https://egemen.kz/last-news?page={}",
        "source": "egemen.kz",
        "type": "global",
        "logo": "https://egemen.kz/img/logo/logo.png",
        "post_data": {
            "title": {"h1": {"class": "responsive_title"}},
            "published_at": {"span": {"class": "text-grey"}},
            "date_format": None,
            "content": {"div": {"class": "main-news padding-80"}},
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
        "pagination_url": "https://kazpravda.kz/r/stati/svezhiy-vypusk",
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
        "base_url": "https://24.kz",
        "is_url_required": True,
        "page_count": 1,
        "pagination_url": "https://24.kz/ru/news",
        "source": "24.kz",
        "type": "global",
        "logo": "https://24.kz/templates/24kz/img/logo-24kz.png",
        "post_data": {
            "title": {"h1": {"class": "single-post__entry-title"}},
            "published_at": {"li": {"class": "entry__meta-date"}},
            "date_format": None,
            "content": {"div": {"class": "entry__article"}},
            "category": None,
            "view_count": None,
            "reaction_count": {"li": {"class": "entry__meta-views"}},
            "image_url": None
        }
    },
]

import json

with open("data_list.json", mode="w", encoding="utf-8") as file:
    json.dump(parser_config_list, file, indent=4, ensure_ascii=False)
