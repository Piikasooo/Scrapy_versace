import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["https://www.versace.com"]
    start_urls = ['https://www.versace.com/us/en-us/home/',]

    def parse(self, response):
        page_link = response.css("li.level-3-item a::attr(href)").getall()
        for i in page_link:
            next_page = response.urljoin(i)
            print(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse_item)

    def parse_item(self, response):
        for item in response.css("div.product-name"):
            yield {
                'name': item.css("a.name-link::text").get(),
                'href': item.css("a.name-link::attr(href)").get(),
            }
