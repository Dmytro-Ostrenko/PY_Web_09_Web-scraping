import scrapy
from .items import AuthorItem

class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for author_link in response.css('div.quote span a::attr(href)').getall():
            yield response.follow(author_link, self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        item = AuthorItem()
        item['fullname'] = response.css('h3.author-title::text').get()
        item['born_date'] = response.css('span.author-born-date::text').get()
        item['born_location'] = response.css('span.author-born-location::text').get()
        item['description'] = response.css('div.author-description::text').get()
        yield item
