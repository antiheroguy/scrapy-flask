
from scrapy import Spider, Request
import os


class WebtruyenSpider(Spider):
    name = 'webtruyen'

    start_urls = [
        'https://webtruyen.com/viet-nu-kiem/viet-nu-kiem_203323.html',
        'https://webtruyen.com/uyen-uong-dao/phan-mot_203324.html',
        'https://webtruyen.com/bach-ma-khieu-tay-phong/chuong-1_747523.html',
        'https://webtruyen.com/tuyet-son-phi-ho/quan-hung-tranh-oat-cai-hop-sat_871449.html',
        'https://webtruyen.com/bich-huyet-kiem/duong-doi-gian-hiem--dan-chung-do-than_202697.html',
        'https://webtruyen.com/lien-thanh-quyet/mung-tho-tinh-kim-ngoc-man-duong_202907.html',
        'https://webtruyen.com/phi-ho-ngoai-truyen/boi-treu-gai-thi-ve-an-don_365290.html',
        'https://webtruyen.com/thu-kiem-an-cuu-luc/phu-dung-cham-nang-giao-ly-mong-ngoc--bach-long-kiem-ha-sat-tieu-van-ky_202646.html',
        'https://webtruyen.com/than-dieu-hiep-lu/phong-nguyet-vo-tinh_488488.html',
        'https://webtruyen.com/anh-hung-xa-dieu/tai-hoa-bat-ngo_37569.html',
        'https://webtruyen.com/than-dieu-dai-hiep/nguoi-di-khach-tren-bo-ho_203177.html',
        'https://webtruyen.com/loc-dinh-ky/phi-lo--chon-phon-hoa-bao-khach-lan-vao_202957.html',
        'https://webtruyen.com/thien-long-bat-bo-ban-moi/mo-dau_491584.html',
        'https://webtruyen.com/tieu-ngao-giang-ho/mo-dau_186152.html',
        'https://webtruyen.com/y-thien-do-long-ky/thien-nhai-tu-quan-bat-kha-vong_378524.html'
    ]

    def parse(self, response, chap=1):
        name = response.xpath(
            '//p[contains(@class, "story-title")]/a/text()').get()
        title = response.xpath(
            '//h2[contains(@class, "chapter-title")]/text()').get()
        content = response.xpath('//div[@id="chapter-content"]').get()

        path = 'outputs/' + name

        if not os.path.exists(path):
            os.makedirs(path)

        if title:
            with open(path + '/' + str(chap) + '.html', 'wb') as file:
                file.write(('<h4>' + title + '</h4>' + content).encode())

        next_page = response.xpath(
            '//div[contains(@class, "chapter-button")]/a[@title="Chương Sau"][not(contains(@class, "disabled"))]/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse, cb_kwargs=dict(chap=chap + 1))
