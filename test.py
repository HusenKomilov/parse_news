# parser_config_list = [
#     {
#         "base_url": "https://daryo.uz",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://daryo.uz/yangiliklar",
#         "source": "daryo.uz",
#         "type": "local",
#         "logo": "https://daryo.uz/logo/logo-white.svg",
#         "post_data": {
#             "title": {"h1": {"class": "is-title post-title post-view-title"}},
#             "published_at": {"time": {"class": "post-date"}},
#             "date_format": None,
#             "content": {"div": {"class": "post-content-wrap has-share-float"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": {"span": {"class": "meta-item post-views has-icon rank-hot"}},
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://kun.uz",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://kun.uz/news/list",
#         "source": "kun.uz",
#         "type": "local",
#         "logo": "4ea914010683e95be91a8074048b3e971c53f30085d454002cd8d0b077b91099.png",
#         "post_data": {
#             "title": {"h1": {"class": "news-inner__content-title"}},
#             "published_at": {"div": {"class": "news-inner__content-stats"}},
#             "date_format": "published_at.split('|')[-1].replace('/','')",
#             "content": {"div": {"class": "news-inner__content-page"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": {"span": {"class": "meta-item post-views has-icon rank-hot"}},
#             "image_url": "img"
#         }
#     },
#     {
#         "base_url": "https://www.gazeta.uz",
#         "is_url_required": True,
#         "page_count": 5,
#         "pagination_url": "https://www.gazeta.uz/oz/list/news?page={}",
#         "source": "gazeta.uz",
#         "type": "local",
#         "logo": "https://www.gazeta.uz/i/gazeta_logo.svg",
#         "post_data": {
#             "title": {"h1": {"itemprop": "headline name"}},
#             "published_at": {"div": {"class": "articleDateTime"}},
#             "date_format": None,
#             "content": {"div": {"class": "js-mediator-article article-text"}},
#             "category": {"span": {"itemprop": "name"}},
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": {"img": {"class": "articleBigPic"}}
#         }
#     },
#     {
#         "base_url": "https://xabar.uz",
#         "is_url_required": False,
#         "page_count": 1,
#         "pagination_url": "https://xabar.uz/yangiliklar",
#         "source": "xabar.uz",
#         "type": "local",
#         "logo": "https://xabar.uz/static/assets/73a7d9c9/img/logo-desktop.svg",
#         "post_data": {
#             "title": {"h2": {"class": "post__title"}},
#             "published_at": {"span": {"class": "date-time"}},
#             "date_format": None,
#             "content": {"div": {"class": "post__body"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": {"div": {"class": "media"}}
#         }
#     },
#     {
#         "base_url": "https://qalampir.uz/uz",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://qalampir.uz/uz/latest",
#         "source": "qalampir.uz",
#         "type": "local",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "text"}},
#             "published_at": None,
#             "date_format": None,
#             "content": {"div": {"class": "row g-4 my-main-content"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": {"img": {"class": "mainImg"}}
#         }
#     },
#     {
#         "base_url": "https://batafsil.uz",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://batafsil.uz/all_news",
#         "source": "batafsil.uz",
#         "type": "local",
#         "logo": "https://batafsil.uz/bitrix/templates/main_2020/images/logo_uz.png",
#         "post_data": {
#             "title": {"h1": {"class": "post-title entry-title"}},
#             "published_at": {"time": {"class": "entry-date published updated"}},
#             "date_format": None,
#             "content": {"div": {"class": "detail-text"}},
#             "category": {"span": {"class": "cat-title"}},
#             "view_count": {"div": {"class": "post-read-time"}},
#             "reaction_count": None,
#             "image_url": {"img": {"class": "attachment-inhype-blog-thumb size-inhype-blog-thumb wp-post-image"}}
#         }
#     },
#     {
#         "base_url": "https://uza.uz/uz",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://uza.uz/uz/posts",
#         "source": "uza.uz",
#         "type": "local",
#         "logo": "https://uza.uz/static/media/uza-logo.c5b4dfd5.svg",
#         "post_data": {
#             "title": {"div": {"class": "news-top-head__title"}},
#             "published_at": {"div": {"class": "news-top-head__date"}},
#             "date_format": "published_at.split('|')[-1].replace('/','')",
#             "content": {"div": {"class": "content-block"}},
#             "category": {"div": {"class": "news-top-head__meta"}},
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": {"img": {"class": "news-top-head__img"}}
#         }
#     },
#     {
#         "base_url": "https://sputniknews.uz",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://sputniknews.uz/news",
#         "source": "sputniknews.uz",
#         "type": "local",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "article__title"}},
#             "published_at": {"div": {"class": "article__info-date"}},
#             "date_format": None,
#             "content": {"div": {"class": "article__body"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://anhor.uz/uzl",
#         "is_url_required": False,
#         "page_count": 1,
#         "pagination_url": "https://anhor.uz/uzl",
#         "source": "anhor.uz",
#         "type": "local",
#         "logo": "https://anhor.uz/wp-content/themes/anhor/assets/img/logo.png",
#         "post_data": {
#             "title": {"h1": {"class": "article__head"}},
#             "published_at": {"span": {"class": "posts-list__date post-meta__item post-meta__date"}},
#             "date_format": None,
#             "content": {"div": {"class": "article__content"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": {"img": {"class": "article__img wp-post-image"}}
#         }
#     },
#     {
#         "base_url": "https://www.norma.uz",
#         "is_url_required": True,
#         "page_count": 3,
#         "pagination_url": "https://www.norma.uz/oz/?page={}&limit=28",
#         "source": "norma.uz",
#         "type": "local",
#         "logo": "https://www.norma.uz/files/norma.uz/images/logo.png",
#         "post_data": {
#             "title": {"h1": {"class": "pos_0"}},
#             "published_at": {"p": {"class": "date"}},
#             "date_format": None,
#             "content": {"div": {"class": "fullText"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://repost.uz/uz",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://repost.uz/uz",
#         "source": "repost.uz",
#         "type": "local",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"itemprop": "headline"}},
#             "published_at": None,
#             "date_format": None,
#             "content": {"div": {"class": "article__content"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://upl.uz",
#         "is_url_required": False,
#         "page_count": 1,
#         "pagination_url": "https://upl.uz",
#         "source": "upl.uz",
#         "type": "local",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "post-title"}},
#             "published_at": {"span": {"itemprop": "datePublished"}},
#             "date_format": None,
#             "content": {"div": {"itemprop": "articleBody"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://uznews.uz/uz",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://uznews.uz/uz/news",
#         "source": "uznews.uz",
#         "type": "local",
#         "logo": "https://uznews.uz/assets/img/logo.svg",
#         "post_data": {
#             "title": {"h1": {"class": "section-header-title title title--m"}},
#             "published_at": {"span": {"class": "section-header-date"}},
#             "date_format": None,
#             "content": {"div": {"class": "content"}},
#             "category": None,
#             "view_count": {"span": {"class": "widgets-item-text"}},
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://rg.ru",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://rg.ru/news.html",
#         "source": "rg.ru",
#         "type": "global",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "PageArticleCommonTitle_title__fUDQW"}},
#             "published_at": {"div": {"class": "ContentMetaDefault_date__wS0te"}},
#             "date_format": None,
#             "content": {"div": {
#                 "class": "PageContentCommonStyling_text__CKOzO commonArticle_text__ul5uZ commonArticle_zoom__SDMjc"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://iz.ru",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://iz.ru/news",
#         "source": "iz.ru",
#         "type": "global",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "m-t-10"}},
#             "published_at": {"div": {"class": "article_page__left__top__time__label"}},
#             "date_format": None,
#             "content": {"div": {
#                 "itemprop": "articleBody"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://www.kp.ru",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://www.kp.ru/online",
#         "source": "kp.ru",
#         "type": "global",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "sc-j7em19-3 eyeguj"}},
#             "published_at": {"span": {"class": "sc-j7em19-1 dtkLMY"}},
#             "date_format": None,
#             "content": {"div": {
#                 "class": "sc-1wayp1z-0 sc-1wayp1z-5 gwmrBl chEeRL"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": {"img": {"class": "sc-foxktb-1 cYprnQ"}}
#         }
#     },
#     {
#         "base_url": "https://aif.ru",
#         "is_url_required": False,
#         "page_count": 1,
#         "pagination_url": "https://aif.ru/news",
#         "source": "aif.ru",
#         "type": "global",
#         "logo": "https://aif.ru/redesign2018/img/logo.svg?14a",
#         "post_data": {
#             "title": {"h1": {"itemprop": "headline"}},
#             "published_at": {"time": {"itemprop": "datePublished"}},
#             "date_format": None,
#             "content": {"div": {
#                 "class": "article_text"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": {"img": {"itemprop": "image"}}
#         }
#     },
#     {
#         "base_url": "https://sputnikglobe.com",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://sputnikglobe.com/news",
#         "source": "sputnikglobe.com",
#         "type": "global",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "article__title"}},
#             "published_at": {"div": {"class": "article__info-date"}},
#             "date_format": None,
#             "content": {"div": {"class": "article__body"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://www.rt.com",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://www.rt.com",
#         "source": "rt.com",
#         "type": "global",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "article__heading"}},
#             "published_at": {"span": {"class": "date date_article-header"}},
#             "date_format": None,
#             "content": {"div": {"class": "article__text text"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://ria.ru",
#         "is_url_required": False,
#         "page_count": 1,
#         "pagination_url": "https://ria.ru",
#         "source": "ria.ru",
#         "type": "global",
#         "logo": None,
#         "post_data": {
#             "title": {"div": {"class": "article__title"}},
#             "published_at": {"div": {"class": "article__info-date"}},
#             "date_format": None,
#             "content": {"div": {"class": "article__body js-mediator-article mia-analytics"}},
#             "category": None,
#             "view_count": {"span": {"class": "article__views"}},
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://www.kommersant.ru",
#         "is_url_required": True,
#         "page_count": 3,
#         "pagination_url": "https://www.kommersant.ru/lenta?from=all_lenta&page={}",
#         "source": "kommersant.ru",
#         "type": "global",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "doc_header__name js-search-mark"}},
#             "published_at": {"time": {"class": "doc_header__publish_time"}},
#             "date_format": None,
#             "content": {"div": {"class": "article_text_wrapper js-search-mark"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://www.vedomosti.ru",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://www.vedomosti.ru",
#         "source": "vedomosti.ru",
#         "type": "global",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "article-headline__title"}},
#             "published_at": {"time": {"class": "article-meta__date"}},
#             "date_format": None,
#             "content": {"div": {"class": "article-boxes-list article__boxes"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://www.gazeta.ru",
#         "is_url_required": True,
#         "page_count": 3,
#         "pagination_url": "https://www.gazeta.ru/news/?p=main&d=1747317476&page={}",
#         "source": "gazeta.ru",
#         "type": "global",
#         "logo": "https://static.gazeta.ru/nm2021/img/logo_2021.svg",
#         "post_data": {
#             "title": {"h1": {"class": "headline"}},
#             "published_at": {"time": {"itemprop": "datePublished"}},
#             "date_format": None,
#             "content": {"div": {"class": "b_article-text"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": {"img": {"class": "item-image"}}
#         }
#     },
#     {
#         "base_url": "https://www.mk.ru",
#         "is_url_required": False,
#         "page_count": 3,
#         "pagination_url": "https://www.mk.ru/news/{}/",
#         "source": "mk.ru",
#         "type": "global",
#         "logo": "https://www.mk.ru/media/mkru2020/img/mk-logo.svg",
#         "post_data": {
#             "title": {"h1": {"class": "article__title"}},
#             "published_at": {"time": {"class": "meta__text"}},
#             "date_format": None,
#             "content": {"div": {"class": "article__body"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": {"img": {"class": "article__picture-image"}}
#         }
#     },
#     {
#         "base_url": "https://www.themoscowtimes.com",
#         "is_url_required": False,
#         "page_count": 1,
#         "pagination_url": "https://www.themoscowtimes.com/news",
#         "source": "themoscowtimes.com",
#         "type": "global",
#         "logo": "https://static.themoscowtimes.com/img/logo_tmt_30_yo.svg",
#         "post_data": {
#             "title": {"header": {"class": "article__header"}},
#             "published_at": {"time": {"class": "byline__datetime timeago"}},
#             "date_format": None,
#             "content": {"div": {"class": "article__block article__block--html article__block--column"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://meduza.io",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://meduza.io",
#         "source": "meduza.io",
#         "type": "global",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "RichTitle-module_root__U5XQu"}},
#             "published_at": {"time": {"class": "Timestamp-module_root__jPJ6w"}},
#             "date_format": None,
#             "content": {"div": {"class": "GeneralMaterial-module-article"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://www.inform.kz",
#         "is_url_required": True,
#         "page_count": 3,
#         "pagination_url": "https://www.inform.kz/lenta/?page={}",
#         "source": "inform.kz",
#         "type": "global",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "article__title"}},
#             "published_at": {"div": {"class": "article__time"}},
#             "date_format": None,
#             "content": {"div": {"class": "article__body-text"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://egemen.kz",
#         "is_url_required": True,
#         "page_count": 3,
#         "pagination_url": "https://egemen.kz/last-news?page={}",
#         "source": "egemen.kz",
#         "type": "global",
#         "logo": "https://egemen.kz/img/logo/logo.png",
#         "post_data": {
#             "title": {"h1": {"class": "responsive_title"}},
#             "published_at": {"span": {"class": "text-grey"}},
#             "date_format": None,
#             "content": {"div": {"class": "main-news padding-80"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://kazpravda.kz",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://kazpravda.kz/r/stati/svezhiy-vypusk",
#         "source": "kazpravda.kz",
#         "type": "global",
#         "logo": None,
#         "post_data": {
#             "title": {"h1": {"class": "article__title"}},
#             "published_at": {"time": {"class": "article__date"}},
#             "date_format": None,
#             "content": {"div": {"class": "article__body"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": None,
#             "image_url": None
#         }
#     },
#     {
#         "base_url": "https://24.kz",
#         "is_url_required": True,
#         "page_count": 1,
#         "pagination_url": "https://24.kz/ru/news",
#         "source": "24.kz",
#         "type": "global",
#         "logo": "https://24.kz/templates/24kz/img/logo-24kz.png",
#         "post_data": {
#             "title": {"h1": {"class": "single-post__entry-title"}},
#             "published_at": {"li": {"class": "entry__meta-date"}},
#             "date_format": None,
#             "content": {"div": {"class": "entry__article"}},
#             "category": None,
#             "view_count": None,
#             "reaction_count": {"li": {"class": "entry__meta-views"}},
#             "image_url": None
#         }
#     },
# ]
# parser_config_list = [
#         {
#             "base_url": "https://general-svr.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://general-svr.com/novosti",
#             "source": "general-svr.com",
#             "type": "global",
#             "logo": "https://general-svr.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "btn btn-default taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://24htoday.net",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://24htoday.net/novosti",
#             "source": "24htoday.net",
#             "type": "global",
#             "logo": "https://24htoday.net/templates/wp/image/logo.png   ",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "btn btn-default taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://mediamonstrosity.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://mediamonstrosity.com/novosti",
#             "source": "mediamonstrosity.com",
#             "type": "global",
#             "logo": "https://mediamonstrosity.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://p-zona.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://p-zona.com/novosti",
#             "source": "p-zona.com",
#             "type": "global",
#             "logo": "https://p-zona.com/templates/wp/img/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://1ubd.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://1ubd.com/novosti",
#             "source": "1ubd.com",
#             "type": "global",
#             "logo": "https://1ubd.com/templates/wp/images/logo.jpg",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://hornbloger.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://hornbloger.com/novosti",
#             "source": "hornbloger.com",
#             "type": "global",
#             "logo": "https://hornbloger.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://insayder2.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://insayder2.com/news",
#             "source": "insayder2.com",
#             "type": "global",
#             "logo": "https://insayder2.com/templates/wp/images/w_logo.png",
#             "post_data": {
#                 "title": {"h2": {"class": "title"}},
#                 "published_at": {"ul": {"class": "tgbanner__content-meta list-wrap"}},
#                 "date_format": "published_at.split(' ')[-1]",
#                 "content": {"div": {"class": "blog-details-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://nahalnews.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://nahalnews.com/novosti",
#             "source": "nahalnews.com",
#             "type": "global",
#             "logo": "https://nahalnews.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "btn btn-default taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://kz-expert.info",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://kz-expert.info",
#             "source": "kz-expert.info",
#             "type": "global",
#             "logo": "https://kz-expert.info/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"div": {"class": "blog-post-title"}},
#                 "published_at": {"div": {"class": "blog-post-time"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "blog-content pb-0"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://compro-r.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://compro-r.com",
#             "source": "compro-r.com",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "single_post_title_main"}},
#                 "published_at": {"span": {"class": "post-date updated"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "post_content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://falshivok.net",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://falshivok.net/novosti",
#             "source": "falshivok.net",
#             "type": "global",
#             "logo": "https://falshivok.net/templates/wp/img/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": None,
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://7-club-7.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://7-club-7.com/novosti",
#             "source": "7-club-7.com",
#             "type": "global",
#             "logo": "https://7-club-7.com/templates/wp/img/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://tlvinsider.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://tlvinsider.com/novosti",
#             "source": "tlvinsider.com",
#             "type": "global",
#             "logo": "https://tlvinsider.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle post_title"}},
#                 "published_at": {"small": {"class": "pull-left"}},
#                 "date_format": "published_at.split(': ')[-1]",
#                 "content": {"div": {"class": "itemFullText"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://sitetalkzone.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://sitetalkzone.com/novosti",
#             "source": "sitetalkzone.com",
#             "type": "global",
#             "logo": "https://sitetalkzone.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": None,
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "http://ru-smi.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "http://ru-smi.com",
#             "source": "ru-smi.com",
#             "type": "global",
#             "logo": "https://ru-smi.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": None,
#                 "date_format": None,
#                 "content": {"div": {"class": "content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://compromat41.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://compromat41.com/novosti",
#             "source": "compromat41.com",
#             "type": "global",
#             "logo": "https://compromat41.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"span": {"class": "itemDateCreated"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://v-kurse2.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://v-kurse2.com",
#             "source": "v-kurse2.com",
#             "type": "global",
#             "logo": "https://v-kurse2.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "main-title"}},
#                 "published_at": {"span": {"class": "text"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://historyofcoins.org",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://historyofcoins.org",
#             "source": "historyofcoins.org",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "http://internetproekt.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "http://internetproekt.com",
#             "source": "internetproekt.com",
#             "type": "global",
#             "logo": "http://internetproekt.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"span": {"class": "itemDateCreated"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "item-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://kontent24.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://kontent24.com",
#             "source": "kontent24.com",
#             "type": "global",
#             "logo": "https://kontent24.com/templates/wp/assets/img/logo-1.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": None,
#                 "date_format": None,
#                 "content": {"div": {"class": "article-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://futlyar.net",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://futlyar.net",
#             "source": "futlyar.net",
#             "type": "global",
#             "logo": "https://futlyar.net/templates/wp/img/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://blogs-exposed.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://blogs-exposed.com",
#             "source": "blogs-exposed.com",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": None,
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://balansst.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://balansst.com",
#             "source": "balansst.com",
#             "type": "global",
#             "logo": "https://balansst.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "btn btn-default taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "http://katarsis7.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "http://katarsis7.com",
#             "source": "katarsis7.com",
#             "type": "global",
#             "logo": "https://katarsis7.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"div": {"class": "blog-post-title"}},
#                 "published_at": {"div": {"class": "post-date-author"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "article-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://tv-lenta.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://tv-lenta.com",
#             "source": "tv-lenta.com",
#             "type": "global",
#             "logo": "https://tv-lenta.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://informanet.org",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://informanet.org",
#             "source": "informanet.org",
#             "type": "global",
#             "logo": "https://informanet.org/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://p-efir.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://p-efir.com",
#             "source": "p-efir.com",
#             "type": "global",
#             "logo": "https://p-efir.com/templates/wp/images/logo-light.png",
#             "post_data": {
#                 "title": {"div": {"class": "blog-post-title"}},
#                 "published_at": {"div": {"class": "blog-post-time"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "blog-content pb-0"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://fayrix.org",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://fayrix.org",
#             "source": "fayrix.org",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": None,
#                 "date_format": None,
#                 "content": {"div": {"class": "item-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://refinancesandiego.org",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://refinancesandiego.org",
#             "source": "refinancesandiego.org",
#             "type": "global",
#             "logo": "https://refinancesandiego.org/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "http://premiumpixel.net",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "http://premiumpixel.net",
#             "source": "premiumpixel.net",
#             "type": "global",
#             "logo": "https://refinancesandiego.org/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "btn btn-default taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://can-explain.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://can-explain.com",
#             "source": "can-explain.com",
#             "type": "global",
#             "logo": "https://can-explain.com/templates/wp/assets/images/logo.png",
#             "post_data": {
#                 "title": {"h3": {"class": "entry-title"}},
#                 "published_at": {"div": {"class": "entry-date"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://politica2.info",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://politica2.info",
#             "source": "politica2.info",
#             "type": "global",
#             "logo": "https://politica2.info/templates/wp/images/logo_sticky.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": None,
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://chatname.net",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://chatname.net",
#             "source": "chatname.net",
#             "type": "global",
#             "logo": "https://chatname.net/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://dvsslco24.org",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://dvsslco24.org",
#             "source": "dvsslco24.org",
#             "type": "global",
#             "logo": "https://dvsslco24.org/templates/wp/image/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": {"a": {"class": "btn btn-default taga"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://persona-l.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://persona-l.com",
#             "source": "persona-l.com",
#             "type": "global",
#             "logo": "https://persona-l.com/templates/wp/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "itemTitle"}},
#                 "published_at": None,
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#     ]

# parser_config_list = [
#         {
#             "base_url": "https://timesofindia.indiatimes.com",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://timesofindia.indiatimes.com",
#             "source": "timesofindia.indiatimes.com",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "HNMDR"}},
#                 "published_at": None,
#                 "date_format": None,
#                 "content": {"div": {"class": "fewcent-121230839 js_tbl_article"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://wan-ifra.org",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://wan-ifra.org/news/page/{}",
#             "source": "wan-ifra.org",
#             "type": "global",
#             "logo": "https://wan-ifra.org/wp-content/themes/wan-ifra/images/logo.png",
#             "post_data": {
#                 "title": "main",
#                 "published_at": None,
#                 "date_format": None,
#                 "content": {"div": {"class": "text"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://kizzyklicks.blogspot.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://kizzyklicks.blogspot.com",
#             "source": "kizzyklicks.blogspot.com",
#             "type": "global",
#             "logo": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0bPZVoqWT43xFqG67jd5lWpGE2kBQ8-s_wyRuPkstHX0jCiUpU-7fJqGRKTPEPVUpLoxTNc5vBUJMhCOSk27rvWSgRK96XheGCYRjvGNJ3ITWyAz8bN98lXdLS-sbWXlT9Wtq8soJ1ztg/s1600/KIZZYKLICKS+NEW.png",
#             "post_data": {
#                 "title": {"h1": {"class": "post-title"}},
#                 "published_at": {"span": {"class": "post-date published"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "post-body post-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://reporter.am",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://reporter.am",
#             "source": "reporter.am",
#             "type": "global",
#             "logo": "https://reporter.am/wp-content/uploads/2022/07/am-reporter-2.png",
#             "post_data": {
#                 "title": {"h1": {"class": "page-title"}},
#                 "published_at": {"span": {"itemprop": "datePublished dateModified"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://internewscast.com",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://internewscast.com",
#             "source": "internewscast.com",
#             "type": "global",
#             "logo": "https://internewscast.com/wp-content/uploads/2025/04/INTERNEWSCAST-icon-1.png",
#             "post_data": {
#                 "title": {"h1": {"class": "entry-title"}},
#                 "published_at": {"time": {"class": "entry-date published"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.npr.org",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://www.npr.org/sections/news/",
#             "source": "npr.org",
#             "type": "global",
#             "logo": "https://static-assets.npr.org/chrome_svg/npr-logo-2025.svg",
#             "post_data": {
#                 "title": {"div": {"class": "storytitle"}},
#                 "published_at": {"span": {"class": "date"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "storytext storylocation linkLocation"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.watchdoguganda.com",
#             "is_url_required": False,
#             "page_count": 3,
#             "pagination_url": "https://www.watchdoguganda.com/category/news/page/{}",
#             "source": "watchdoguganda.com",
#             "type": "global",
#             "logo": "https://www.watchdoguganda.com/wp-content/uploads/2019/01/logo-1-1-1.png",
#             "post_data": {
#                 "title": {"h1": {"class": "jeg_post_title"}},
#                 "published_at": {"div": {"class": "jeg_meta_date"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "content-inner"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://africalaunchpad.com",
#             "is_url_required": False,
#             "page_count": 3,
#             "pagination_url": "https://africalaunchpad.com/news/page/{}",
#             "source": "africalaunchpad.com",
#             "type": "global",
#             "logo": "https://africalaunchpad.com/wp-content/uploads/2022/12/africa-launch-pad-logo249x85.webp",
#             "post_data": {
#                 "title": {"h1": {"class": "entry-title"}},
#                 "published_at": {"p": {"class": "post-modified-info"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://worldcelebritynews.com",
#             "is_url_required": False,
#             "page_count": 3,
#             "pagination_url": "https://worldcelebritynews.com/category-list?page={}",
#             "source": "worldcelebritynews.com",
#             "type": "global",
#             "logo": "https://worldcelebritynews.com/storage/img-9672-removebg-preview-2.png",
#             "post_data": {
#                 "title": {"h1": {"class": "post-title"}},
#                 "published_at": {"span": {"class": "post-on has-dot"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "ck-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.latimes.com",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://www.latimes.com",
#             "source": "latimes.com",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "headline"}},
#                 "published_at": {"span": {"class": "published-date-day"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "ct-rich-text-children font-cmsFontBrandText font-normal text-lg leading-7.75 [&_>p]:text-cms-story-body-color-text clearfix mb-10 md:max-w-170 md:mx-auto"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://quintdaily.com",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://quintdaily.com",
#             "source": "quintdaily.com",
#             "type": "global",
#             "logo": "https://quintdaily.com/wp-content/uploads/2021/06/Quintdaily-Logo-1.png",
#             "post_data": {
#                 "title": {"h1": {"class": "entry-title"}},
#                 "published_at": {"span": {"class": "td-post-date"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "td-post-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.theunionjournal.com",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://www.theunionjournal.com",
#             "source": "theunionjournal.com",
#             "type": "global",
#             "logo": "https://cdn.shortpixel.ai/spai/q_lossy+w_150+to_auto+ret_img/www.theunionjournal.com/wp-content/uploads/2020/11/test-logo-4-150x150-1.png",
#             "post_data": {
#                 "title": {"h1": {"class": "entry-title"}},
#                 "published_at": {"time": {"class": "entry-date updated td-module-date"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "markdown prose w-full break-words dark:prose-invert dark"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.dainikviral.com",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://www.dainikviral.com",
#             "source": "dainikviral.com",
#             "type": "global",
#             "logo": "https://www.dainikviral.com/wp-content/uploads/2023/08/cropped-cropped-cropped-cropped-cropped-Dainik-Viral-Picture-1.png",
#             "post_data": {
#                 "title": {"h1": {"class": "entry-title"}},
#                 "published_at": {"time": {"class": "entry-date published"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://bbcbreakingnews.com",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://bbcbreakingnews.com",
#             "source": "bbcbreakingnews.com",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "title"}},
#                 "published_at": None,
#                 "date_format": None,
#                 "content": {"article": {"class": "small single"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.worldpresslive.com",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://www.worldpresslive.com",
#             "source": "worldpresslive.com",
#             "type": "global",
#             "logo": "https://www.worldpresslive.com/wp-content/uploads/2022/06/WORD-PRESS-LIVE-01.png",
#             "post_data": {
#                 "title": {"h1": {"class": "post-title single-post-title entry-title"}},
#                 "published_at": {"time": {"class": "entry-date published"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "inner-post-entry entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.akinblog.com",
#             "is_url_required": False,
#             "page_count": 3,
#             "pagination_url": "https://www.akinblog.com/page/{}",
#             "source": "akinblog.com",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "title single"}},
#                 "published_at": {"span": {"class": "mg-blog-date"}},
#                 "date_format": None,
#                 "content": {"article": {"class": "page-content-single small single"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#     ]

# parser_config_list = [
#         {
#             "base_url": "https://www.bbc.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://www.bbc.com",
#             "source": "bbc.com",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "sc-f98b1ad2-0 dfvxux"}},
#                 "published_at": {"time": {"class": "sc-801dd632-2 IvNnh"}},
#                 "date_format": None,
#                 "content": {"div": {"data-component": "text-block"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://syrianwar1.blogspot.com",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://syrianwar1.blogspot.com",
#             "source": "syrianwar1.blogspot.com",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h3": {"class": "post-title entry-title"}},
#                 "published_at": {"h2": {"class": "date-header"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "post-body entry-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://edition.cnn.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://edition.cnn.com",
#             "source": "edition.cnn.com",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "headline__text inline-placeholder vossi-headline-text"}},
#                 "published_at": {"div": {"class": "timestamp vossi-timestamp"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "article__content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://rhymes-punches.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://rhymes-punches.com",
#             "source": "rhymes-punches.com",
#             "type": "global",
#             "logo": "https://rhymes-punches.com/templates/wp/img/logo.png",
#             "post_data": {
#                 "title": {"div": {"class": "blog-post-title"}},
#                 "published_at": {"div": {"class": "post-date-author"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "article-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://asiaplustj.info",
#             "is_url_required": True,
#             "page_count": 3,
#             "pagination_url": "https://asiaplustj.info/ru/news/all?page={}",
#             "source": "asiaplustj.info",
#             "type": "global",
#             "logo": "https://asiaplustj.info/sites/all/themes/asiaplus/images/logo-front.png?v4",
#             "post_data": {
#                 "title": {"h1": {"class": "atitle"}},
#                 "published_at": {"div": {"class": "article-info"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "article-body js-mediator-article"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://astanatv.kz",
#             "is_url_required": True,
#             "page_count": 3,
#             "pagination_url": "https://astanatv.kz/kz/news/?page={}",
#             "source": "astanatv.kz",
#             "type": "global",
#             "logo": "https://astanatv.kz/assets/astanatv-logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "news__title xl-mb-20 xs-mb-20"}},
#                 "published_at": {"div": {"class": "news__date xl-mr-20"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "news-full-text"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://kazpravda.kz",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://kazpravda.kz",
#             "source": "kazpravda.kz",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "article__title"}},
#                 "published_at": {"time": {"class": "article__date"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "article__body"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://iz.ru",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://iz.ru/news",
#             "source": "iz.ru",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"itemprop": "headline"}},
#                 "published_at": {"div": {"class": "article_page__left__top__time__label"}},
#                 "date_format": None,
#                 "content": {"div": {"itemprop": "articleBody"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.trend.az",
#             "is_url_required": False,
#             "page_count": 1,
#             "pagination_url": "https://www.trend.az/latest/",
#             "source": "trend.az",
#             "type": "global",
#             "logo": "https://www.trend.az/assets/img/logo30.svg?v558",
#             "post_data": {
#                 "title": {"div": {"class": "top-part"}},
#                 "published_at": {"span": {"class": "date-time"}},
#                 "date_format": None,
#                 "content": {"div": {"itemprop": "articleBody"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.ozodlik.org",
#             "is_url_required": True,
#             "page_count": 3,
#             "pagination_url": "https://www.ozodlik.org/z/421?p={}",
#             "source": "ozodlik.org",
#             "type": "global",
#             "logo": "72a38011d72261932735c12480557d8274d34635e2c28eee2ab1f58ab0f3b39a.png",
#             "post_data": {
#                 "title": {"h1": {"class": "title pg-title"}},
#                 "published_at": {"span": {"class": "date"}},
#                 "date_format": None,
#                 "content": {"div": {"id": "article-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": {"span": {"class": "meta-item post-views has-icon rank-hot"}},
#                 "image_url": "img"
#             }
#         },
#         {
#             "base_url": "https://www.newsru.com",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://www.newsru.com/allnews",
#             "source": "newsru.com",
#             "type": "global",
#             "logo": "https://static.newsru.com/static/v3/img/misc/rucom_main.png",
#             "post_data": {
#                 "title": {"h1": {"class": "article-title"}},
#                 "published_at": {"div": {"class": "article-date"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "article-text"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://niann.ru",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://niann.ru",
#             "source": "niann.ru",
#             "type": "global",
#             "logo": "https://niann.ru/_data/objects/0000/0170/icon.png",
#             "post_data": {
#                 "title": {"h1": {"class": "header"}},
#                 "published_at": {"span": {"class": "date_standart date"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "mess_standart"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.chechnyafree.ru",
#             "is_url_required": False,
#             "page_count": 3,
#             "pagination_url": "https://www.chechnyafree.ru/page/{}",
#             "source": "chechnyafree.ru",
#             "type": "global",
#             "logo": None,
#             "post_data": {
#                 "title": {"h1": {"class": "entry-title"}},
#                 "published_at": {"time": {"class": "entry-date published updated"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "entry-content clearfix"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://24.kg",
#             "is_url_required": True,
#             "page_count": 3,
#             "pagination_url": "https://24.kg/page_{}",
#             "source": "24.kg",
#             "type": "global",
#             "logo": "https://24.kg/assets/7a772a43/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "newsTitle"}},
#                 "published_at": {"span": {"itemprop": "datePublished"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "cont"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.inopressa.ru",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://www.inopressa.ru",
#             "source": "inopressa.ru",
#             "type": "global",
#             "logo": "https://static.inopressa.ru/img/inopressa-logo-light.gif",
#             "post_data": {
#                 "title": {"div": {"class": "topic"}},
#                 "published_at": {"div": {"class": "maincaption"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "body"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.ntv.ru",
#             "is_url_required": True,
#             "page_count": 3,
#             "pagination_url": "https://www.ntv.ru/novosti?page={}",
#             "source": "ntv.ru",
#             "type": "global",
#             "logo": "https://static2.ntv.ru/static/images/logo.png",
#             "post_data": {
#                 "title": {"h1": {"class": "h h-l content-top__title"}},
#                 "published_at": {"p": {"class": "cap cap-xs content-top__date"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "content-text"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://www.rosbalt.ru",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://www.rosbalt.ru/news",
#             "source": "rosbalt.ru",
#             "type": "global",
#             "logo": "https://files.1mi.media/39de3f037a203dee014c6bddc7d37b5804aacd91/resize:auto:0:0:0/c41a92fe9ea4f6991bbf9950fe6fa3fa53e9bfd31ef1bef46d9b59f9398a.svg",
#             "post_data": {
#                 "title": {"h1": {"class": "MatterTopNoImage_title___N52h"}},
#                 "published_at": {"div": {"class": "MatterTopNoImage_date__u0xOz"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "mb-[24px] lg:mb-[36px] content-blocks kind-common"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://alisnad.com",
#             "is_url_required": False,
#             "page_count": 3,
#             "pagination_url": "https://alisnad.com/page/{}",
#             "source": "alisnad.com",
#             "type": "global",
#             "logo": "https://alisnad.com/wp-content/uploads/2020/01/Logo-no-com-300x98.png",
#             "post_data": {
#                 "title": {"h1": {"class": "entry-title"}},
#                 "published_at": {"time": {"class": "entry-date updated td-module-date"}},
#                 "date_format": None,
#                 "content": {"div": {"class": "td-post-content"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#         {
#             "base_url": "https://vasudeva.ru",
#             "is_url_required": True,
#             "page_count": 1,
#             "pagination_url": "https://vasudeva.ru",
#             "source": "vasudeva.ru",
#             "type": "global",
#             "logo": "https://vasudeva.ru/images/logo251.jpg",
#             "post_data": {
#                 "title": {"h1": {"itemprop": "headline"}},
#                 "published_at": {"time": {"itemprop": "datePublished"}},
#                 "date_format": None,
#                 "content": {"div": {"itemprop": "articleBody"}},
#                 "category": None,
#                 "view_count": None,
#                 "reaction_count": None,
#                 "image_url": None
#             }
#         },
#     ]
# import json
#
# with open("data_list3.json", mode="w", encoding="utf-8") as file:
#     json.dump(parser_config_list, file, indent=4, ensure_ascii=False)

