
from crawler.items.EbookItem import EbookItem
from scrapy import Spider, Request
from scrapy.selector import Selector
import os


class IsachSpider(Spider):
    name = 'isach'

    base_url = 'https://isach.info/'

    start_urls = [
        'https://isach.info/story.php?list=story&author=kim_dung',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse_group)

    def parse_group(self, response):
        group = response.xpath(
            '//div[contains(@class, "ms_list_item")]//div[contains(@class, "left_list_item")]/a[starts-with(@href, "http")]/@href').getall()
        i = 0
        for url in group:
            i = i + 1
            yield Request(url + '&chapter=0000', callback=self.parse_list)

    def parse_list(self, response):
        list = response.xpath(
            '//div[@id="motsach_content_body"]//div[contains(@class, "right_menu_item")]/a/@href').getall()
        i = 0
        for url in list:
            i = i + 1
            yield Request(self.base_url + url, callback=self.parse_item, cb_kwargs=dict(chap=i))

    def parse_item(self, response, chap):
        name = response.xpath(
            '//div[@id="motsach_content_body"]//div[contains(@class, "ms_title")]/a/text()').get()
        title = response.xpath(
            '//div[@id="motsach_content_body"]//div[contains(@class, "ms_chapter")]/text()').get()
        content = '</p><p>'.join(response.xpath(
            '//div[@id="motsach_content_body"]//div[contains(@class, "ms_chapter")]//following-sibling::div[not(contains(@class, "navigator_bottom"))]/text()').getall())
        dropcap = response.xpath('//div[@id="dropcap"]//text()').get()

        full_content = dropcap + content if dropcap else content

        path = 'outputs/' + name

        if not os.path.exists(path):
            os.makedirs(path)

        if title:
            with open(path + '/' + str(chap) + '.html', 'wb') as file:
                file.write(('<h4>' + title + '</h4><p>' +
                            full_content + '</p>').encode())

        return EbookItem(
            title=title,
            content=content
        )
