from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider


class OECDSpider(PostHTMLSpider):
    name = 'oecd'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0',
    }

    start_urls = [
        'https://www.oecd.org/newsroom/publicationsdocuments/bydate/'
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//div[contains(@class, "last")]/li/div/div/h4/a'), callback='parse_page'),
    ]

    xpath_content = '(//div[@id="webEditContent"] | //div[@id="mainContent"]//div[@class="content"] | //div[contains(@class, "entry-summary")])'
