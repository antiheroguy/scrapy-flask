from crawler.spiders.base.PostSpider import PostSpider
from scrapy.http import Request
from scrapy.spiders import XMLFeedSpider


class PostRSSSpider(PostSpider, XMLFeedSpider):
    feed = 'RSS'

    itertag = 'item'

    iterlink = 'link/text()'

    def parse_node(self, response, node):
        link = node.xpath(self.iterlink).extract_first()
        if link:
            if hasattr(self, 'baselink'):
                link = self.baselink + link
            return Request(link.strip(), self.parse_page)
        else:
            self.logger.error('No URL found')
