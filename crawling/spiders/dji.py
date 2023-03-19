from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'dji'

    #for dji.com
    allowed_domains = ['www.dji.com'] 
    start_urls = ['https://www.dji.com/ru']
    base_url = 'https://www.dji.com/ru'
    count = 0
    same = set()
    crawled_pages = set()

    rules = [
        Rule(LinkExtractor(allow=r"ru/(.*?)site=brandsite&from=nav"), callback="parse_item")
             ]

    def parse_item(self, response):
        exists = response.xpath('//a[@data-ga-label="buy_now"]').extract_first()
        if exists:
            pass
            #parse here
