from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class EuropaSpider(PostHTMLSpider):
    name = 'europa'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0'
    }

    start_urls = [
        'https://ec.europa.eu/international-partnerships/newsroom/news',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//li[contains(@class, "ecl-pager__item--current")]/following-sibling::*[1]/self::li[contains(@class, "ecl-pager__item")]//a'), follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='//a[contains(@class, "ecl-list-item__link")]'), callback='parse_page'),
    ]

    xpath_content = '//div[contains(@class, "ecl-paragraph")]'
