from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class ExpochTimesSpider(PostRSSSpider):
    name = 'expochtimes'

    start_urls = [
        'https://www.epochtimes.jp/nimpart.xml'
    ]

    xpath_content = '//div[contains(@class, "page_content")]'
