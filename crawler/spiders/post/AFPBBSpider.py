from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class AFPBBSpider(PostRSSSpider):
    name = 'afpbb'

    start_urls = [
        'https://feeds.afpbb.com/rss/afpbb/afpbbnews'
    ]

    xpath_content = '//div[contains(@class, "article-body")]'
