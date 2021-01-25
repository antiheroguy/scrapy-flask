# -*- coding: utf-8 -*-
from crawler.items.EbookItem import EbookItem
from scrapy import Spider, Request
from scrapy.selector import Selector
import os


class EtruyenSpider(Spider):
    name = 'etruyen'

    base_url = 'http://etruyen.com/'

    start_urls = [
        'http://etruyen.com/index.php?tacgiaid=y&page=284'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse_group)

    def parse_group(self, response):
        group = response.xpath(
            '//li[contains(@class, "menutruyen")]/a/@href').getall()
        for url in group:
            yield Request(self.base_url + url, callback=self.parse_list)

    def parse_list(self, response):
        list = response.xpath(
            '//div[contains(@class, "blog-sidebar")]/div[contains(@class, "list-group")][1]/a[@href]').getall()
        i = 0
        for item in list:
            url = Selector(text=item).xpath('//@href').get()
            if url:
                i = i + 1
                yield Request(self.base_url + url, callback=self.parse_item, cb_kwargs=dict(chap=i))

    def parse_item(self, response, chap):
        name = response.xpath(
            '//div[contains(@class, "page-header")]//text()').get().strip('\n').strip(' ')
        title = response.xpath('//h4').get()
        content = ''.join(response.xpath(
            '//div[contains(@class, "truyen_text")]/div').getall())

        path = 'outputs/' + name

        if not os.path.exists(path):
            os.makedirs(path)

        if title:
            with open(path + '/' + str(chap) + '.html', 'wb') as file:
                file.write((title + content).encode())

        return EbookItem(
            title=title,
            content=content
        )
