from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider


class JIJISpider(PostHTMLSpider):
    name = 'jiji'

    start_urls = [
        'https://www.jiji.com/jc/list?g=pol',
        'https://www.jiji.com/jc/list?g=eco',
        'https://www.jiji.com/jc/list?g=afp'
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//ul[contains(@class, "LinkList")]//li//a'), callback='parse_page'),
    ]

    xpath_content = '//div[contains(@class, "ArticleText")]'
