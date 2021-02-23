import scrapy


class BigfileSpider(scrapy.Spider):
    name = 'bigfile'
    allowed_domains = ['debian.org']
    start_urls = ['http://debian.org/']

    def parse(self, response):
        pass
