# -*- coding: utf-8 -*-
from crawler.items.EbookItem import EbookItem
from scrapy import Spider, Request
from scrapy.selector import Selector
import os


class SStruyenSpider(Spider):
    name = 'sstruyen'

    base_url = 'https://sstruyen.com'

    start_urls = [
        'https://sstruyen.com/tac-gia/kim-dung/trang-1/',
        'https://sstruyen.com/tac-gia/kim-dung/trang-2/',
        'https://sstruyen.com/tac-gia/kim-dung/trang-3/',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse_group)

    def parse_group(self, response):
        group = response.xpath(
            '//div[contains(@class, "inner-item")]/a/following-sibling::*[1]/self::a/@href').getall()
        for url in group:
            newUrl = 'https://sstruyen.com/ajax.php?get_chapt&story_seo=' + \
                url.strip('/') + '&chapt=1'
            yield Request(newUrl, callback=self.parse_list)

    def parse_list(self, response):
        list = response.xpath('//select/option').getall()
        i = 0
        for item in list:
            url = Selector(text=item).xpath('//@value').get()
            i = i + 1
            yield Request(self.base_url + url, callback=self.parse_item, cb_kwargs=dict(chap=i))

    def parse_item(self, response, chap):
        name = response.xpath(
            '//h1[contains(@class, "rv-full-story-title")]//text()').get()
        title = response.xpath(
            '//div[contains(@class, "rv-chapt-title")]//a/text()').get()
        content = ''.join(response.xpath(
            '//div[contains(@class, "content_wrap1")]/div[contains(@class, "content")][1]').getall())

        path = 'outputs/' + name

        if not os.path.exists(path):
            os.makedirs(path)

        if title:
            with open(path + '/' + str(chap) + '.html', 'wb') as file:
                file.write(('<h4>' + title + '</h4>' + content).encode())

        return EbookItem(
            title=title,
            content=content
        )
