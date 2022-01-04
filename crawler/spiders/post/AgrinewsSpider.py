from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class AgrinewsSpider(PostHTMLSpider):
    name = 'agrinews'

    start_urls = [
        'https://www.agrinews.co.jp/news',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//div[contains(@class, "uk-grid")]//a'), callback='parse_page'),
    ]

    xpath_content = '//div[contains(@class, "article_detail")]'
