from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class EMBJapanSpider(PostHTMLSpider):
    name = 'embjapan'

    start_urls = [
        'https://www.un.emb-japan.go.jp/itpr_ja/index.html',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//div[@id="section2"]//ul[contains(@class, "linklist_date")]//li//a'), callback='parse_page'),
    ]

    xpath_content = '//div[contains(@class, "main-section")]//div[contains(@class, "any-area")]'
