from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class VietJoSpider(PostRSSSpider):
    name = 'vietjo'

    iterator = 'xml'

    itertag = 'p:item'

    iterlink = 'p:link/text()'

    namespaces = [('p', 'http://purl.org/rss/1.0/')]

    start_urls = [
        'https://www.viet-jo.com/rss/headline.rdf'
    ]

    xpath_content = '//p[@id="vj_content"]'
