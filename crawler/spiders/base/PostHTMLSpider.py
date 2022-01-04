from crawler.spiders.base.PostSpider import PostSpider
from scrapy.spiders import CrawlSpider


class PostHTMLSpider(PostSpider, CrawlSpider):
    feed = 'HTML'
