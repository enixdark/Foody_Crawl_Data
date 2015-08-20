# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider , Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from bs4 import BeautifulSoup, Comment
from scrapy.conf import settings
from selenium import webdriver
import time
from ..items import FoodyItem
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class FoodySpider(CrawlSpider):
	name = "foody"
	allowed_domains = [
		"www.foody.vn",
	]

	start_urls = [
		'http://www.foody.vn/',
	]

	

	__queue = [
		'top-thanh-vien$'
	]

	rules = [
	    Rule(
	    	LinkExtractor(allow=(
	    		r'[-\w]+\/',
	    		r'bo-suu-tap\/[-.\w\/]+',
	    		r'bo-suu-tap\/w+',
	    	), deny=__queue,
	    	restrict_xpaths=[
	    		r'//ul[@class="vietnam-regions-list"]/li/a',
	    		r'//div[@class="profile-collection-container1"]/div/div[1]/a[1]'
	    	]), 
	    	callback='parse_extract_data_city', follow=True
	    	)
	    ]


	def __init__(self,*args, **kwargs):
		super(FoodySpider, self).__init__(*args, **kwargs)
		# dcap = dict(DesiredCapabilities.PHANTOMJS)
		# dcap["phantomjs.page.settings.userAgent"] = settings.get("USER_AGENT_LIST")
		# self.driver = webdriver.PhantomJS(desired_capabilities=dcap)
		self.driver = webdriver.Firefox()
		self.countries = []
		self.main_url = 'http://www.foody.vn'

	
	def start_requests(self):
		if self.countries == []:
			self.driver.get(self.main_url)
			time.sleep(3)
			self.driver.find_element_by_class_name("dropdown1").find_element_by_tag_name('a').click()
			self.countries = Selector(text=self.driver.page_source).xpath('//ul[@class="vietnam-regions-list"]/li/a/@href').extract()
			self.driver.close()
		# for url in self.countries:
		# 	yield Request(self.main_url + url, callback=self.parse)
		requests = list(super(FoodySpider, self).start_requests())
		requests += [Request(self.main_url + url, self.parse_extract_data_city) for url in self.countries]
		return requests


	# def start_urls(self,response):
	



	def parse_extract_data_city(self, response):
	    food_list = response.xpath('//div[@id="user-wish-list"]/div/div[3]/div')
    	    if food_list:
    	    	import ipdb; ipdb.set_trace()
		_datas = FoodyItem()
		_datas['list'] = []
		for food in food_list:
		    item = FoodyItem()
		    item['name'] = ''.join(food.xpath('.//div[@class="collection-detail-list-full-item-heading"]/div[2]/h2/a/text()').extract())
		    _data_address = ''.join(food.xpath('.//div[@class="collection-detail-list-item-information"]/div[1]/span[2]/text()').extract()).split(',')
		    if len(_data_address) == 4:
		    	_data_address = [_data_address[0], _data_address[1]  + _data_address[2], _data_address[3]]
                    elif len(_data_address) == 5:
		    	_data_address = [_data_address[0] + _data_address[1],_data_address[2]   + _data_address[3], _data_address[4]]
		    item['address'], item['lane'], item['city'] = _data_address
		    item['phone'] = ''.join(food.xpath('.//div[@class="collection-detail-list-item-information"]/div[2]/span[2]/text()').extract())
		    item['price_start'] = ''.join(food.xpath('.//div[@class="collection-detail-list-item-information"]/div[3]/span[2]/span[1]/text()').extract())
		    item['price_end'] = ''.join(food.xpath('.//div[@class="collection-detail-list-item-information"]/div[3]/span[2]/span[2]/span[1]/text()').extract())
                    _datas['list'].append(item)
		return _datas

	# def parse_extract_food(self,response):



