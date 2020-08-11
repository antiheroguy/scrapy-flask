# -*- coding: utf-8 -*-
from crawler.items.PostItem import PostItem
from scrapy import Spider, Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
import json


class BongdaSpider(CrawlSpider):
    name = 'bongda'

    start_urls = ['http://www.bongda.com.vn/tin-moi-nhat/']

    rules = [
        Rule(LinkExtractor(
            restrict_xpaths='//ul[contains(@class, "list_news_cate")]//li//a[contains(@class, "title_list_top_news")]'), callback='parse_item')
    ]

    def __init__(self, **kwargs):
        start_urls = []
        for url in self.start_urls:
            for i in range(1, 2):
                new_url = url if i == 1 else url + 'p' + str(i)
                start_urls.append(new_url)

        self.start_urls = start_urls
        super().__init__(**kwargs)

    def parse_item(self, response):
        title = response.xpath(
            '//h1[contains(@class, "time_detail_news")]//a//text()').get().strip('\n').strip(' ')
        content = ''.join(response.xpath(
            '//article[@id="content_detail"]/div/p//text()').getall())
        return PostItem(
            title=title,
            content=content
        )
