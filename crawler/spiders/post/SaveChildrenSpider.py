from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class SaveChildrenSpider(PostHTMLSpider):
    name = 'savechildren'

    start_urls = [
        'https://www.savechildren.or.jp/news/index.html'
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//ul[@id="info_blk"]/li[count(preceding-sibling::*)=0]/ul/li//a'), callback='parse_page'),
    ]

    xpath_content = '//div[contains(@class, "entry")]/div[contains(@class, "entry-content")]'

    xpath_description = '//meta[@name="description"]//@content | //meta[@name="Description"]//@content'
