from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class WorldVisionSpider(PostHTMLSpider):
    name = 'worldvision'

    start_urls = [
        'https://www.worldvision.jp/news/',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//li[@class="news_headline"]/following-sibling::*[1]/self::a'), follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='//li[@class="news_headline"]/a'), callback='parse_page'),
    ]

    xpath_content = '//div[@id="contents"]'
