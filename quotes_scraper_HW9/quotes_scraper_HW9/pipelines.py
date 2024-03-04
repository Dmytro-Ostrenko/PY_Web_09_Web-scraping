# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class QuotesScraperHw9Pipeline:
    def process_item(self, item, spider):
        return item

# import json

# class SaveToJsonPipeline:
#     def open_spider(self, spider):
#         self.quotes_file = open('quotes.json', 'w')
#         self.authors_file = open('authors.json', 'w')

#         self.quotes_data = []
#         self.authors_data = []

#     def close_spider(self, spider):
#         json.dump(self.quotes_data, self.quotes_file)
#         json.dump(self.authors_data, self.authors_file)

#         self.quotes_file.close()
#         self.authors_file.close()

#     def process_item(self, item, spider):
#         if 'quote' in item and 'author' in item and 'tags' in item:
#             self.quotes_data.append(dict(item))
#         elif 'fullname' in item and 'born_date' in item and 'born_location' in item and 'description' in item:
#             self.authors_data.append(dict(item))
#         return item
