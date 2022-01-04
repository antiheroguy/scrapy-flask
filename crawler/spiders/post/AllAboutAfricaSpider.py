from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider


class AllAboutAfricaSpider(PostHTMLSpider):
    name = 'allaboutafrica'

    start_urls = [
        'https://all-about-africa.com/category/news/',
        'https://all-about-africa.com/?s='
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//article//div[contains(@class, "post-title")]//a'), callback='parse_page'),
    ]

    xpath_content = '//div[@class="content"]'

    counter = 3

    def sitemap_filter(self, entries):
        for entry in entries:
            if '/sitemap-pt-post' in entry['loc']:
                self.counter -= 1
                if self.counter >= 0:
                    yield entry
            else:
                yield entry

    def parse_site(self, response):
        pass
