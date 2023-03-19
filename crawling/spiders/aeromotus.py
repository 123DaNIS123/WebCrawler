from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'aeromotus'
    #for aeromotus
    allowed_domains = ['aeromotus.ru'] 
    start_urls = ['https://aeromotus.ru/shop/']
    base_url = 'https://aeromotus.ru/shop/'

    rules = [
        Rule(LinkExtractor(allow="product/"), callback="parse_item"),
        Rule(LinkExtractor(allow="page/", deny="add-to-cart", unique=True), follow=True)
             ]

    def parse_item(self, response):
        #parse here
        pass
