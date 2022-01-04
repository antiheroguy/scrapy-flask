from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class JbicSpider(PostHTMLSpider):
    name = 'jbic'

    start_urls = [
        'https://www.jbic.go.jp/ja/information/press/index.html',
        'https://www.jbic.go.jp/ja/information/news/index.html',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//main//div[contains(@class, "main")]//a'), callback='parse_page'),
    ]
