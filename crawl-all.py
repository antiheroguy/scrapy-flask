from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from crawler.spiders.post.VogueSpider import VogueSpider
from crawler.spiders.post.WorldVisionSpider import WorldVisionSpider

process = CrawlerProcess(get_project_settings())
process.crawl(VogueSpider)
process.crawl(WorldVisionSpider)
process.start()
