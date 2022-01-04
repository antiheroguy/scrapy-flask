from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class GanasSpider(PostRSSSpider):
    name = 'ganas'

    start_urls = [
        'https://www.ganas.or.jp/feed/'
    ]

    xpath_content = '//div[contains(@class, "single_in")]'
