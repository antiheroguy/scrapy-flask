from crawler.spiders.base.PostSitemapSpider import PostSitemapSpider


class BBCSpider(PostSitemapSpider):
    name = 'bbc'

    sitemap_urls = [
        'https://www.bbc.com/sitemaps/https-index-com-news.xml'
    ]

    sitemap_rules = [
        ('/japanese/', 'parse_page'),
    ]

    xpath_content = '//main'
