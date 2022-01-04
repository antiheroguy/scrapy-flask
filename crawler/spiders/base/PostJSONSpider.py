from crawler.spiders.base.PostSpider import PostSpider
from scrapy.http import Request
import json


class PostJSONSpider(PostSpider):
    feed = 'json'

    def parse(self, response):
        body = json.loads(response.body)
        data = self.deep_get(body, self.list_path) if hasattr(
            self, 'list_path') else body

        if isinstance(data, list) and hasattr(self, 'limit'):
            data = data[:self.limit]

        for entry in data:
            item = entry if isinstance(entry, dict) else data[entry]
            url = self.deep_get(item, self.item_path) if hasattr(
                self, 'item_path') else item

            if url:
                if hasattr(self, 'base_path'):
                    url = self.base_path + url
                yield Request(url, self.parse_page)

    def deep_get(self, d, keys, default=None):
        if d is None:
            return default
        if not keys:
            return d
        return self.deep_get(d.get(keys[0]), keys[1:], default)
