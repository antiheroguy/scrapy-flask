from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class JicaSpider(PostRSSSpider):
    name = 'jica'

    start_urls = [
        'https://www.jica.go.jp/feed/jicanews.xml',
        'https://www.jica.go.jp/nagoya-hiroba/feed/news.xml',
        'https://www.jica.go.jp/hiroba/feed/news.xml',
        'https://www.jica.go.jp/jica-ri/ja/news/rss/rss.xml',
    ]

    xpath_content = '(//div[@id="mainCol"] | //div[@id="main"]/div | //div[@id="mainColumn"]//div[contains(@class, "sentence")] | //article//div[contains(@class, "sentence")])'
