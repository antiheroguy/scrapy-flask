from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class IADBSpider(PostHTMLSpider):
    name = 'iadb'

    start_urls = [
        'https://www.iadb.org/en/news',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//ul[contains(@class, "pager__items")]/li[contains(@class, "pager__item--next")]/a', allow=r'page=\d{1}$'), follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='//div[contains(@class, "search-results")]//a'), callback='parse_page'),
    ]

    xpath_title = '///div[contains(@class, "news-title")]//text()'

    xpath_content = '//main//div[contains(@class, "field--type-text-with-summary")]'
