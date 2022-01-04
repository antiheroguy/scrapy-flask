from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class WFPSpider(PostHTMLSpider):
    name = 'wfp'

    start_urls = [
        'https://wfp.org/news',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//ol[contains(@class, "pagination--wrapper")]/li[contains(@class, "pager__item--next")]/a', allow=r'&page=\d{1}$'), follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='//article[contains(@class, "news-teaser")]/a', deny=r'news\?'), callback='parse_page'),
    ]

    xpath_content = '//div[contains(@class, "layout--content")]'
