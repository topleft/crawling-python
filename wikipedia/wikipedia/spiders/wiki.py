# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector

from wikipedia.items import WikipediaItem

from urlparse import urljoin


class BasicSpider(Spider):
    # name the spider
    name = "wiki"

    # allowed domains to scrape
    allowed_domains = ["en.wikipedia.org"]

    # urls the spider begins to crawl from
    start_urls = ["http://en.wikipedia.org/wiki/Category:2016_films"]

    # parses and returns the scraped data
    def parse(self, response):

        titles = Selector(response).xpath('//div[@id="mw-pages"]//li')

        for title in titles:
            item = WikipediaItem()
            url = title.xpath("a/@href").extract()
            item["title"] = title.xpath("a/text()").extract()
            if type(url) is list and len(url) is 1:
                item["url"] = urljoin("http://en.wikipedia.org", url[0])
            else:
                item["url"] = "NO URL AVAILABLE"
            yield item
