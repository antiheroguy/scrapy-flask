from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class UNICEFSpider(PostHTMLSpider):
    name = 'unicef'

    start_urls = [
        'https://www.unicef.or.jp/index.html'
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//div[contains(@class, "news_area")]/div/a'), follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='//ul[contains(@class, "bec")]/li/a'), callback='parse_page'),
    ]

    xpath_content = '//div[contains(@class, "news_content")]'
