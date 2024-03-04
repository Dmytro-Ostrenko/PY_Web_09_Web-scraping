
# BOT_NAME = "quotes_scraper_HW9"
# SPIDER_MODULES = ["quotes_scraper_HW9.spiders"]
# NEWSPIDER_MODULE = "quotes_scraper_HW9.spiders"
# USER_AGENT = "quotes_scraper_HW9 (+http://www.yourdomain.com)"
# ROBOTSTXT_OBEY = True
# REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# FEED_EXPORT_ENCODING = "utf-8"

BOT_NAME = 'quotes_scraper_HW9'

SPIDER_MODULES = ['quotes_scraper_HW9.spiders']
NEWSPIDER_MODULE = 'quotes_scraper_HW9.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'quotes_scraper_HW9 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'quotes_scraper_HW9.pipelines.QuotesScraperHw9Pipeline': 300,
}

# Configure output format and file names for quotes and authors
FEED_FORMAT = 'json'
FEED_URI = 'quotes.json'  # For quotes
# FEED_URI = 'authors.json'  # For authors