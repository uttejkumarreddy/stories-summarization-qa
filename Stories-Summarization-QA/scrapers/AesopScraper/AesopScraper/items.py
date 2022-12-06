# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AesopscraperItem(scrapy.Item):
    title = scrapy.Field()
    story = scrapy.Field()
    moral = scrapy.Field()