from crawler.spiders.base.PostJSONSpider import PostJSONSpider


class WorldBankSpider(PostJSONSpider):
    name = 'worldbank'

    start_urls = [
        'https://search.worldbank.org/api/v2/news?format=json&rows=100&fct=displayconttype_exact,topic_exact,lang_exact,count_exact,countcode_exact,admreg_exact&src=cq55&apilang=en&lang_exact=English',
    ]

    xpath_content = '//div[contains(@class, "c14v1-body")]'

    list_path = ['documents']

    item_path = ['url']
