from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class CNNSpider(PostRSSSpider):
    name = 'cnn'

    iterator = 'xml'

    itertag = 'p:item'

    iterlink = 'p:link/text()'

    namespaces = [('p', 'http://purl.org/rss/1.0/')]

    start_urls = [
        'https://feeds.cnn.co.jp/rss/cnn/cnn.rdf'
    ]

    xpath_content = '//div[@id="leaf-body"]'
