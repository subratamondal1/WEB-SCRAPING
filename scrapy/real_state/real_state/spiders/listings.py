import scrapy
from real_state.items import RealStateItem


class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['arizonarealestate.com']
    start_urls = [
        'http://arizonarealestate.com/maricopa',
        'http://arizonarealestate.com/goodyear',
        'http://arizonarealestate.com/tempe'
    ]

    # scraping logic goes here
    def parse(self, response):
        gallery = response.xpath("//div[@class='si-listings-column']")

        for listing in gallery:
            item = RealStateItem()

            item["name"] = listing.xpath(
                "//div[@class='si-listing__title-main']/text() | //div[@class='si-listing__neighborhood']/span[@class='si-listing__neighborhood-place']/text()").getall()

            item["description"] = listing.xpath(
                "//div[@class='si-listing__title-description']/text()").get()

            item["price"] = listing.xpath(
                "//div[@class='si-listing__photo-price']/span/text()").get()

            item["agency"] = listing.xpath(
                "//div[@class='si-listing__footer']/div/text()").get()

            yield item
