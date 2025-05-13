import scrapy

class QuantScraperItem(scrapy.Item):
    # Title of the article or post
    title = scrapy.Field()
    
    # URL of the scraped content
    url = scrapy.Field()
    
    # Main body or content of the page
    content = scrapy.Field()
    
    # Date when the article was published
    publish_date = scrapy.Field()
    
    # Name of the author or source
    author = scrapy.Field()
