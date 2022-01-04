from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class MofaSpider(PostHTMLSpider):
    name = 'mofa'

    start_urls = [
        'https://www.mofa.go.jp/press/release/index.html',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//div[@id="main"]//ul[contains(@class, "link-list")]//a'), callback='parse_page'),
    ]

    xpath_content = '//div[contains(@class, "main-section")]//div[contains(@class, "any-area")]'
