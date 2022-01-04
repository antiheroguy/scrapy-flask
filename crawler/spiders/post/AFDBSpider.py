from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class AFDBSpider(PostRSSSpider):
    name = 'afdb'

    start_urls = [
        'https://www.afdb.org/en/news-and-events/rss'
    ]
