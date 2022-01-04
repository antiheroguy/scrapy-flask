from crawler.spiders.base.PostRSSSpider import PostRSSSpider


class UsaidSpider(PostRSSSpider):
    name = 'usaid'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0'
    }

    start_urls = ['https://www.usaid.gov/rss/speeches.xml']

    xpath_content = '//div[contains(@class, "field-name-body")]//div//div[contains(@class, "field-item")]'
