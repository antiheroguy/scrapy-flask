from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider


class JapanPlatformSpider(PostHTMLSpider):
    name = 'japanplatform'

    start_urls = [
        'https://www.japanplatform.org/info/'
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//div[contains(@class, "content")]//dd/a', allow=r'/info/'), callback='parse_page'),
    ]
