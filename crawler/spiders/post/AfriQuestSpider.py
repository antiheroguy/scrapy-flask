from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class AfriQuestSpider(PostRSSSpider):
    name = 'afriquest'

    start_urls = ['https://afri-quest.com/feed']

    xpath_content = '//div[contains(@class, "td-post-content")]'
