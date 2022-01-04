from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class UNDPSpider(PostHTMLSpider):
    name = 'undp'

    start_urls = [
        'https://www.jp.undp.org/content/tokyo/ja/home/presscenter/_jcr_content/mainPar/newsCentreList.html?s=0&c=100',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//div[contains(@class, "main-section")]/h4/a'), callback='parse_page'),
    ]

    xpath_content = '//section[@id="generic-content"]//div[contains(@class, "section text")]'
