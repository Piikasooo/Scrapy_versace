import scrapy
from ..items import Product, Href
from scrapy.loader import ItemLoader


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'feed-test.csv'
    }

    start_urls = ['https://www.versace.com/us/en-us/home/', ]

    def parse(self, response):
        link = ItemLoader(item=Href(), response=response)
        link.add_css('href', "li.view-all-item a::attr(href)")
        return link.load_item()

    def parse_item(self, response):
        product = ItemLoader(item=Product(), response=response)
        product.add_css('name', "h1.product-name::text")
        product.add_css('price', "span.js-sl-price::text")
        product.add_css('description', "div.product-description::text")
        return product.load_item()





