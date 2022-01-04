from crawler.spiders.base.PostSpider import PostSpider
from dateutil import parser
from scrapy.http import Request
from scrapy.spiders import SitemapSpider
from scrapy.utils.sitemap import Sitemap, sitemap_urls_from_robots
import logging

logger = logging.getLogger(__name__)


class PostSitemapSpider(PostSpider, SitemapSpider):
    feed = 'sitemap'

    def _parse_sitemap(self, response):
        if response.url.endswith('/robots.txt'):
            for url in sitemap_urls_from_robots(response.text, base_url=response.url):
                yield Request(url, callback=self._parse_sitemap)
        else:
            body = self._get_sitemap_body(response)
            if body is None:
                logger.warning("Ignoring invalid sitemap: %(response)s", {
                               'response': response}, extra={'spider': self})
                return

            s = Sitemap(body)
            it = self.sitemap_filter(s)

            if s.type == 'sitemapindex':
                for node in self.iterloc(it):
                    loc = node['loc']
                    if any(x.search(loc) for x in self._follow):
                        yield Request(loc, callback=self._parse_sitemap)
            elif s.type == 'urlset':
                for node in self.iterloc(it):
                    loc = node['loc']
                    for r, c in self._cbs:
                        if r.search(loc):
                            yield Request(loc, callback=c, meta={'lastmod': node['lastmod']})
                            break

    def iterloc(self, it):
        def to_timestamp(x): return parser.isoparse(x).timestamp()

        for d in it:
            lastmod = to_timestamp(d['lastmod']) if 'lastmod' in d else 0
            yield {
                'loc': d['loc'],
                'lastmod': lastmod
            }

            # Also consider alternate URLs (xhtml:link rel="alternate")
            if self.sitemap_alternate_links and 'alternate' in d:
                for l in d['alternate']:
                    yield {
                        'loc': l,
                        'lastmod': lastmod
                    }
