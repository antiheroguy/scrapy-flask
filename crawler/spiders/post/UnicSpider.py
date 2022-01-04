from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class UnicSpider(PostHTMLSpider):
    name = 'unic'

    start_urls = [
        'https://www.unic.or.jp/news_press/info/'
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//div[contains(@class, "pagination01")]/span[contains(@class, "current")]/following-sibling::*[1]/self::a', allow=r'page\/\d{1}\/'), follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='//ul[contains(@class, "entry_list01")]//li//a'), callback='parse_page'),
    ]

    xpath_content = '//div[@id="cm_content"]//div[contains(@class, "entry")]'
