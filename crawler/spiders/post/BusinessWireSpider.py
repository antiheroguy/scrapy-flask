from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class BusinessWireSpider(PostHTMLSpider):
    name = 'businesswire'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0'
    }

    start_urls = [
        'https://www.businesswire.com/portal/site/home/news/language/?vnsId=32413',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//div[contains(@class, "pagingNext")]/a', allow=r'\*G\d{1}\*'), follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='//a[contains(@class, "bwTitleLink")]'), callback='parse_page'),
    ]

    xpath_content = '//div[contains(@class, "bw-release-body")]'
