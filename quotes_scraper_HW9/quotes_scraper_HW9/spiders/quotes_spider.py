import scrapy
from .items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['quote'] = quote.css('span.text::text').get()
            item['author'] = quote.css('span small.author::text').get()
            item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)