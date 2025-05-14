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

    # [Incremental] Tags or categories associated with the article
    tags = scrapy.Field()

    # [Incremental] Short summary or abstract of the content
    summary = scrapy.Field()

    # [Incremental] Credibility score or source reliability metric
    credibility_score = scrapy.Field()

