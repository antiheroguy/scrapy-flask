from crawler.spiders.base.PostHTMLSpider import PostHTMLSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class ReutersSpider(PostHTMLSpider):
    name = 'reuters'

    start_urls = [
        'https://jp.reuters.com/news/archive/worldNews?view=page&page=1&pageSize=10',
        'https://jp.reuters.com/news/archive/technologyNews?view=page&page=1&pageSize=10',
        'https://jp.reuters.com/news/archive/oddlyEnoughNews?view=page&page=1&pageSize=10',
        'https://jp.reuters.com/news/archive/businessNews?view=page&page=1&pageSize=10',
        'https://jp.reuters.com/news/archive/domesticJPNews?view=page&page=1&pageSize=10',
    ]

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//a[contains(@class, "control-nav-next")]', allow=r'&page=\d{1}&'), follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='//article//div[contains(@class, "story-content")]//a'), callback='parse_page'),
    ]

    xpath_content = '//div[contains(@class, "ArticleBodyWrapper")]'

    xpath_unnecessary = [
        '//figure',
        '//div[contains(@class, "ArticleBody-byline-container")]',
        '/div[descendant::button[contains(@class, "Slideshow-inline-image-container")]]'
    ]
