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
        for next_page in response.css("li.view-all-item a::attr(href)").getall():
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_link_on_item)

        for next_page in response.css("li.children-category a.subcategory-image-link::attr(href)").getall():
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_link_on_item)

    def parse_link_on_item(self, response):
        for next_page in response.css("ul.search-result-items li.js-grid-tile "
                                      "div.product-information-wrapper div.product-name a::attr(href)").getall():
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse_item)

    def parse_item(self, response):
        product = ItemLoader(item=Product(), response=response)
        product.add_css('name', "h1.product-name::text")
        product.add_css('price', "span.js-sl-price::text")
        product.add_css('description', "div.product-description::text")
        return product.load_item()





