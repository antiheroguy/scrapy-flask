from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider


class JapanHeartSpider(PostHTMLSpider):
    name = 'japanheart'

    start_urls = [
        'https://www.japanheart.org/topics/',
        'https://www.japanheart.org/reports/',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//div[@id="pagenation"]//span[contains(@class, "current")]/following-sibling::*[1]/self::a', allow=r'page\/\d{1}\/'), follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='//div[@id="topics-inner"]/dl/dt/a'), callback='parse_page'),
        Rule(LinkExtractor(
            restrict_xpaths='//div[@id="topics-inner"]//div[contains(@class, "topics-content")]/a'), callback='parse_page'),
    ]

    xpath_content = '//div[contains(@class, "entry-body")]'
