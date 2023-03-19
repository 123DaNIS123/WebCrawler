from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'myspider'
    # for aeromotus
    # allowed_domains = ['aeromotus.ru'] 
    # start_urls = ['https://aeromotus.ru/shop/']
    # base_url = 'https://aeromotus.ru/shop/'
    # count = 0
    # same = set()
    # crawled_pages = set()

    # rules = [
    #     Rule(LinkExtractor(allow="product/"), callback="parse_item"),
    #     Rule(LinkExtractor(allow="page/", deny="add-to-cart", unique=True), follow=True, callback="page_number")
    #          ]

    #for NELK
    allowed_domains = ['nelk.ru'] 
    start_urls = ['https://nelk.ru/catalog/robototekhnicheskie_sistemy/bespilotnye_aviatsionnye_sistemy/']
    base_url = 'https://nelk.ru/catalog/robototekhnicheskie_sistemy/bespilotnye_aviatsionnye_sistemy/'
    count = 0
    same = set()
    crawled_pages = set()

    rules = [
        Rule(LinkExtractor(allow="nelk"), callback="parse_number")
        # Rule(LinkExtractor(allow="page/", deny="add-to-cart", unique=True), follow=True, callback="page_number")
             ]

    def parse_item(self, response):
        print(response.url)
        title = response.url
        if title in self.same:
            print("\n\n\n\n\nit's the same!!!!",title)
        else:
            self.same.add(title)
        self.count += 1
        print(title)
        print("REAL COUNT: ", len(self.same))
        print("not good count: ", self.count)

    def page_number(self, response):
        self.crawled_pages.add(response.url)
        print("page number is", response.url)
        print(self.crawled_pages)
