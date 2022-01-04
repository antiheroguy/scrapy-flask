from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class SustainableJapanSpider(PostRSSSpider):
    name = 'sustainablejapan'

    start_urls = [
        'https://sustainablejapan.jp/feed',
    ]

    xpath_content = '//div[contains(@class, "entry-content")]'
