import scrapy
from ..items import Product
from scrapy.loader import ItemLoader


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'feed-test.csv'
    }
    allowed_domains = ["https://www.versace.com/"]
    start_urls = ['https://www.versace.com/us/en-us/jeans-couture/new-arrivals/new-in-for-her/logo-belt-bag-e899/EE1VVBBL3-E71411_ENU_NR_E899__.html?cgid=11000041#start=1', ]

    def parse(self, response):
        product = ItemLoader(item=Product(), response=response)
        product.add_css('name', "h1.product-name::text")
        product.add_css('price', "span.js-sl-price::text")
        product.add_css('description', "div.product-description::text")
        return product.load_item()





