import scrapy
import json
import logging
from scrapy.crawler import CrawlerProcess

class ScraperQuotesSpider(scrapy.Spider):
    name = 'scraper_quotes' # назва павука
    domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com'] # URL-адрес для початку сканування
    
    def __init__(self):
        super().__init__() # ініціалізація павука
        # створення списку для зберігання цитат і авторів
        self.quotes = []
        self.authors = {}
        logging.basicConfig(level=logging.INFO)     
    
    def parse(self, response): # метод для обробки відповіді від сервера
        quotes = response.css('div.quote')
        
        for quote in quotes:
            quote_data = {'tags': quote.css('div.tags a.tag::text').getall(),
                'author': quote.css('span small.author::text').get(),
                'quote': quote.css('span.text::text').get(),}
            self.quotes.append(quote_data)

            author_name = quote_data['author']
            if author_name not in self.authors:
                author_link = quote.css('span a::attr(href)').get()
                yield response.follow(author_link, self.parse_author, meta={'author_name': author_name})

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        else:
            self.save_to_json()     
    
    def parse_author(self, response):  # метод для обробки інформації про автора
        author_name = response.request.meta['author_name']
        born_date = response.css('span.author-born-date::text').get()
        born_location = response.css('span.author-born-location::text').get()
        description = response.css('div.author-description::text').get()

        self.authors[author_name] = {
            'fullname': author_name,
            'born_date': born_date.strip() if born_date else None,
            'born_location': born_location.strip() if born_location else None,
            'description': description.strip() if description else None
        }

    #перетворення до тексту json формату та записом
    def save_to_json(self):
        with open('quotes.json', 'w') as f:
            json.dump(self.quotes, f, indent="\t")

        with open('authors.json', 'w') as f:
            #json.dump(list(self.authors.values()), f, indent="\t", ensure_ascii=False)
            json.dump(list(self.authors.values()), f, indent="\t")

if __name__ == "__main__":
    # Створюємо процес запуску пауки
    process = CrawlerProcess()
    # запуск павука
    process.crawl(ScraperQuotesSpider)
    # Ззапуск процесу
    process.start()



