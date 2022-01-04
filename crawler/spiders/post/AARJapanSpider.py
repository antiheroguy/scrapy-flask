from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class AARJapanSpider(PostRSSSpider):
    name = 'aarjapan'

    iterator = 'xml'

    itertag = 'p:entry'

    iterlink = 'p:link/@href'

    namespaces = [('p', 'http://www.w3.org/2005/Atom')]

    start_urls = [
        'https://www.aarjapan.gr.jp/activity/report/atom.xml'
    ]

    xpath_content = '//div[@id="main"]'
