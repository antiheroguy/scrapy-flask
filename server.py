from scrapy.signals import item_scraped
from scrapy.signalmanager import dispatcher
from scrapy.crawler import CrawlerRunner
from flask import Flask, jsonify
from crawler.spiders.post.CNNSpider import CNNSpider
import crochet

crochet.setup()

app = Flask(__name__)
data = []


def process_result(item, response, spider):
    data.append(dict(item))


@app.route('/post', methods=['GET'])
def scape_post():
    scrape_with_crochet(
        spider=CNNSpider
    )

    return jsonify(data)


@crochet.wait_for(timeout=60.0)
def scrape_with_crochet(spider):
    global data
    data = []
    crawl_runner = CrawlerRunner()
    dispatcher.connect(process_result, signal=item_scraped)
    return crawl_runner.crawl(spider)


if __name__ == '__main__':
    app.run(debug=True)
