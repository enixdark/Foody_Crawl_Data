# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.conf import settings
from scrapy import log
from .models import models




class FoodyPipeline(object):
    def process_item(self, item, spider):
    	for _item in item['list']:
           new = models.FoodyModel(
           	name = _item['name'],
           	address = _item['address'],
           	price_start = _item['price_start'],
           	price_end = _item['price_end'],
                lane = _item['lane'],
                phone = _item['phone'],
                city = _item['city']
           )
           new.save()
        return item
