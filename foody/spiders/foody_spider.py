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

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class FoodySpider(CrawlSpider):
	name = "foody"
	allowed_domains = [
		"www.foody.vn",
	]

	start_urls = [
		'http://www.foody.vn/',
	]

	

	__queue = []

	rules = [
	    Rule(
	    	LinkExtractor(allow=(
	    		'[-\w]+\/',
	    		'bo-suu-tap\/[-\w]+\/',
	    		'bo-suu-tap\/w+',
	    	), deny=__queue,
	    	restrict_xpaths=[
	    		'//ul/li/a',
	    		'//div[@class="profile-collection-container1"]/div/div/a[1]'
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
		
		item = scrapy.Item()

		return item

	# def parse_extract_food(self,response):



