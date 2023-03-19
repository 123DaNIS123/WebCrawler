from scrapy import Spider

class MySpider(Spider):
    name = 'myspider_old_old'
    allowed_domains = ['aeromotus.ru']
    start_urls = ['https://aeromotus.ru/shop/']

    def parse(self, response):
        for product in response.css("a.woocommerce-loop-product__link"):
            link_ro_product = product.css("::attr(href)").get()
            print(link_ro_product)

            yield response.follow(link_ro_product, callback=self.parse_product())

        next_page = response.css("a.next::attr(href)").get()
