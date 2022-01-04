from crawler.spiders.base.PostSitemapSpider import PostSitemapSpider


class VogueSpider(PostSitemapSpider):
    name = 'vogue'

    sitemap_urls = [
        'https://www.vogue.co.jp/sitemap.xml'
    ]

    sitemap_rules = [
        ('/article/', 'parse_page'),
        ('/gallery/', 'parse_page'),
    ]

    xpath_content = '(//div[@data-test-id="GalleryBody"] | //div[@data-test-id="ArticleLayout"])'
