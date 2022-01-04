from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class EIBSpider(PostRSSSpider):
    name = 'eib'

    start_urls = [
        'https://www.eib.org/en/press/news/index.rss',
        'https://www.eib.org/en/press/all/index.rss',
        'https://www.eib.org/en/blog/index.rss'
    ]

    xpath_content = '//div[contains(@class, "post-text-wrapper")]'
