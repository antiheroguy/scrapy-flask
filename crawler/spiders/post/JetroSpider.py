from crawler.spiders.base.PostSitemapSpider import PostSitemapSpider


class JetroSpider(PostSitemapSpider):
    name = 'jetro'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0'
    }

    sitemap_urls = [
        'https://www.jetro.go.jp/sitemap.xml'
    ]

    sitemap_rules = [
        ('/biznews/', 'parse_page'),
    ]

    xpath_content = '//div[contains(@class, "wzg")]'
