# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodyItem(scrapy.Item):
    list = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    lane = scrapy.Field()
    city = scrapy.Field()
    phone = scrapy.Field()
    price_start = scrapy.Field()
    price_end = scrapy.Field()
