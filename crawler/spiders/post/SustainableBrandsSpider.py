from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class SustainableBrandsSpider(PostRSSSpider):
    name = 'sustainablebrands'

    iterator = 'xml'

    itertag = 'item'

    iterlink = 'path/text()'

    baselink = 'https://www.sustainablebrands.jp'

    start_urls = [
        'https://www.sustainablebrands.jp/mod/xml/news_all.xml',
    ]

    xpath_content = '//article//section'
