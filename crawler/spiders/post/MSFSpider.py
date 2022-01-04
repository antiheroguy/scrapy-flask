from crawler.spiders.base.PostJSONSpider import PostJSONSpider


class MSFSpider(PostJSONSpider):
    name = 'msf'

    start_urls = [
        'https://www.msf.or.jp/news/json/news_headline.json',
        'https://www.msf.or.jp/news/json/news_pressrelease.json'
    ]

    xpath_content = '//div[contains(@class, "main-inner")]'

    item_path = ['anc', 'href']

    base_path = 'https://www.msf.or.jp'

    limit = 20
