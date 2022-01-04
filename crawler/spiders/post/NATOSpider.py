from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class NATOSpider(PostRSSSpider):
    name = 'nato'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0'
    }

    start_urls = [
        'https://www.nato.int/cps/rss/en/natohq/rssFeed.xsl/rssFeed.xml'
    ]

    xpath_content = '//section[contains(@class, "content")]'
