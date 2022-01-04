from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class ADBSpider(PostHTMLSpider):
    name = 'adb'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0'
    }

    start_urls = [
        'https://www.adb.org/ja/offices/japan/news',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//div[contains(@class, "views-list")]/ul/li/div/span/a'), callback='parse_page'),
    ]
