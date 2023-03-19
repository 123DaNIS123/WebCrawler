from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'geobox'
    #for geobox
    allowed_domains = ['www.geobox.ru'] 
    start_urls = ['https://geobox.ru/catalog/']
    base_url = 'https://geobox.ru/catalog/'
    count = 0
    same = set()
    crawled_pages = set()

    rules = [
        Rule(LinkExtractor(allow="catalog/"), callback="parse_item")
             ]

    def parse_item(self, response):
        exists = response.xpath('//a[@title="В корзину"]').extract_first()
        if exists:
            print(response.url)
            print("exists")
            self.count += 1
            self.same.add(response.url)
            print(self.count)
            print(len(self.same))
            if self.count == 41:
                print(self.same)
