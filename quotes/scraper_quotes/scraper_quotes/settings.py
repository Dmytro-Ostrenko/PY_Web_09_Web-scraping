# BOT_NAME = "scraper_quotes"

# SPIDER_MODULES = ["scraper_quotes.spiders"]
# NEWSPIDER_MODULE = "scraper_quotes.spiders"
# # Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# FEED_EXPORT_ENCODING = "utf-8"


# Scrapy settings for quotes_scraper_HW9 project

BOT_NAME = 'quotes_scraper'


SPIDER_MODULES = ['scraper_quotes.spiders']
NEWSPIDER_MODULE = 'scraper_quotes.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'quotes_scraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# # Configure output format and file names for quotes and authors
# FEEDS = {
#     'quotes.json': {
#         'format': 'json',
#         'overwrite': True,
#     },
#     'authors.json': {
#         'format': 'json',
#         'overwrite': True,
#     },
# }