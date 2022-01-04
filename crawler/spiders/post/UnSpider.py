from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class UnSpider(PostRSSSpider):
    name = 'un'

    start_urls = [
        'https://news.un.org/feed/subscribe/en/news/all/rss.xml'
    ]

    xpath_content = '//div[contains(@class, "entity-paragraphs-item")]//div[contains(@class, "field-item")]'
