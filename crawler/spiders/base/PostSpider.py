from crawler.items.PostItem import PostItem
from scrapy import signals
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join
from scrapy.spiders import Spider
from urllib.parse import urlparse
import re


class PostSpider(Spider):
    xpath_title = '(//meta[@property="og:title"]//@content | //h1//text())'

    xpath_description = '//meta[@name="description"]//@content'

    xpath_image = '//meta[@property="og:image"]//@content'

    xpath_content = '//article'

    xpath_unnecessary = []

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(PostSpider, cls).from_crawler(
            crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_opened,
                                signal=signals.spider_opened)
        crawler.signals.connect(spider.spider_closed,
                                signal=signals.spider_closed)
        return spider

    def parse_page(self, response):
        if hasattr(response, 'selector'):
            selector = response.selector
            loader = ItemLoader(item=PostItem(), selector=selector)
            for xpath in self.xpath_unnecessary:
                for node in response.selector.root.xpath(self.xpath_content + xpath):
                    node.getparent().remove(node)

            def trim(x): return x.strip()
            def convert_url(x): return convert_path('"' + x).strip('"')

            def convert_path(x):
                uri = urlparse(response.url)
                relative_path = uri.path[:uri.path.rfind('/')]
                base_url = '{uri.scheme}://{uri.netloc}'.format(uri=uri)
                base_path = '{uri.scheme}://{uri.netloc}{relative_path}'.format(
                    uri=uri, relative_path=relative_path)
                # Convert path start with '//' to full path
                x = re.sub(r'(\'|\"|\()\/\/',  r'\g<1>' + 'https://', x)
                # Convert relative path start with '/' to absolute path
                x = re.sub(r'(\'|\"|\()\/', r'\g<1>' + base_url + '/', x)
                # Convert relative path start with '../' or './' to absolute path
                x = re.sub(r'(\'|\"|\()(\.+\/)', r'\g<1>' +
                           base_path + '/' + r'\g<2>', x)
                # Force https for http url
                x = re.sub(r'(http)(:\/\/)', r'\g<1>s\g<2>', x)
                # Force relative src (like: 'src="image/demo.png"') to absolute src
                x = re.sub(r'(src|href)=(\"|\')((?!http).)',
                           r'\g<1>=\g<2>' + base_path + '/' + r'\g<3>', x)
                # Force relative url (like: 'url(demo)') to absolute src
                x = re.sub(r'(url\((\"|\')?)((?!http).)',
                           r'\g<1>' + base_path + '/' + r'\g<3>', x)
                # Replace duplicate in schema (like: 'src="https://abc.com/https://abc.com/demo"')
                x = re.sub(r'(https?:\/\/.+\/){2}', r'\g<1>', x)
                return x

            loader.add_value('url', response.url)
            loader.add_xpath('title', self.xpath_title, TakeFirst(), trim)
            loader.add_xpath('image', self.xpath_image,
                             TakeFirst(), trim, convert_url)
            loader.add_xpath('content',
                             self.xpath_content, TakeFirst(), trim, convert_path)
            loader.add_xpath('description',
                             self.xpath_description + ' | ' + self.xpath_content + '//p[1]//text()', TakeFirst(), trim)
            loader.add_xpath('text_only',
                             self.xpath_content + '//text()', Join(''), trim)

            item = loader.load_item()

            print(item['url'])

            return item

    def spider_opened(spider):
        print('Start crawling: ' + spider.name)

    def spider_closed(spider):
        print('End crawling: ' + spider.name)
