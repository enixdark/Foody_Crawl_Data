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
import re

class FoodySpider(CrawlSpider):
	name = "foody"
	allowed_domains = [
		"www.foody.vn",
	]

	start_urls = [
		'http://www.foody.vn',
		'http://www.foody.vn/ha-noi/nha-hang'
	]

	

	__queue = [
		r'(.?)page=[23456789]'
	]

	rules = [
	    Rule(
	    	LinkExtractor(allow=(
	    		# r'[-\w]+\/',
	    		r'bo-suu-tap\/[-.?=\w\/]+',
	    		r'ha-noi\/[-.?=\w]+',
	    		r'ha-noi\/[-.?=\w]+\/',
	    	), deny=__queue,
	    	restrict_xpaths=[
	    		# r'//div[6]/section[1]/div/div/div/div[2]/div/div[3]',
	    		# r'//div[6]/section[1]/div/div/div/div[2]/div',
	    		# r'//div[6]/section[2]/div/div/div/div/div[1]/div[1]/div/div/div[1]',
	    		# r'//div[6]/section[2]/div/div/div/div/div[1]/div[3]/div/div/div/div[3]/div/div/div[3]/div',
	    		# r'//div[6]/section[2]/div/div/div/div/div[1]/div[3]/div/div/div/div[3]/div/div/div[4]',
	    		# r'//div[6]/section[2]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div',
	    		# r'//div[6]/section[2]/div/div/div/div/div[1]/div[4]/div/div'
	    	]), 
	    	callback='parse_extract_data_city', follow=True
	    	)
	    ]

	
	def extract(self,sel,xpath):
		try:
			text = sel.xpath(xpath).extract()
			return re.sub(r"\s+", "", ''.join(text).strip(), flags=re.UNICODE)

		except Exception, e:
			raise Exception("Invalid XPath: %s" % e)


	def parse_extract_data_city(self, response):
		item = None
		try:
			if ('khu-vuc' not in response.url) and ('bo-suu-tap' not in response.url):
				sel = response.xpath('//div[6]')
				item = FoodyItem()
				item['url'] = response.url
				item['title'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[2]/h1//text()')
				item['address'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[4]/div[1]/div/div//text()')
			    # lane = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[3]/div/div[2]/div[1]//text()')
			    # city = self.extract(sel,'//text()')
			    # phone = self.extract(sel,'//text()')
				item['time_start'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[4]/div[3]/div[1]/span[3]/span/span[1]//text()')
				item['time_end'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[4]/div[3]/div[1]/span[3]/span/span[2]//text()')
				item['price_start']= self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[4]/div[3]/div[2]/span[2]/span//text()')
				item['price_end'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[4]/div[3]/div[2]/span[2]/span/span//text()')
				item['image'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[1]/div/a/img/@src')

				item['total_write_review'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[2]/div[1]/div[1]/ul/li[1]/a[2]/span//text()')
				item['total_upload_images'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[2]/div[1]/div[1]/ul/li[2]/a[2]/span//text()')
				item['total_check_in'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[2]/div[1]/div[1]/ul/li[3]/a[2]/span//text()')
				item['total_save_to_love_collection'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[2]/div[1]/div[1]/ul/li[4]/a[2]/span//text()')
				item['total_save_to_wish_collection'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[2]/div[1]/div[1]/ul/li[5]/a[2]/span//text()')
				item['total_save_to_custom_collections'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[2]/div[1]/div[1]/ul/li[6]/a[2]/span//text()')


				item['score_space'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/span//text()')
				item['score_quality'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/span//text()')
				item['score_price'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[3]/div/div[3]/div[1]/span//text()')
				item['score_service'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[3]/div/div[4]/div[1]/span//text()')
				item['score_location'] = self.extract(sel,'//section[1]/div/div/div/div[2]/div/div[4]/div[2]/div/div[1]/div[3]/div/div[5]/div[1]/span//text()')

				item['total_score_comment_for_excellent'] = self.extract(sel,'//section[2]/div/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/a/span[1]/b//text()')
				item['total_score_comment_for_good'] = self.extract(sel,'//section[2]/div/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/a/span[1]/b//text()')
				item['total_score_comment_for_avg'] = self.extract(sel,'//section[2]/div/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[3]/a/span[1]/b//text()')
				item['total_score_comment_for_bad'] = self.extract(sel,'//section[2]/div/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[4]/a/span[1]/b//text()')
				item['avg_score_comment'] = self.extract(sel,'//section[2]/div/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div[1]/div[5]/div/span/b//text()')

				geo = self.extract(sel,'//a[@class="linkmap"]/img/@src').split('_')
				item['geo_latitude'] = geo[-2].replace('-','.')
				item['geo_longitude'] = geo[-1].replace('-','.').replace('.jpg','')

				item['types'] = self.extract(sel,'//div[@class="new-detail-info-sec"][2]/div[1]/div[2]//text()')
				item['dining_time'] = self.extract(sel,'//div[@class="new-detail-info-sec"][1]/div[2]/div[2]//text()')
				item['last_order'] = self.extract(sel,'//div[@class="new-detail-info-sec"][1]/div[3]/div[2]//text()')
				item['waiting_time'] =self.extract(sel,'//div[@class="new-detail-info-sec"][1]/div[4]/div[2]//text()')
				item['holiday'] = self.extract(sel,'//div[@class="new-detail-info-sec"][1]/div[5]/div[2]//text()')
				item['capacity'] = self.extract(sel,'//div[@class="new-detail-info-sec"][2]/div[2]/div[2]//text()')
				item['cuisine_style']  = self.extract(sel,'//div[@class="new-detail-info-sec"][2]/div[3]/div[2]//text()')
				item['good_for'] = self.extract(sel,'//div[@class="new-detail-info-sec"][2]/div[4]/div[2]//text()')
				item['typical_dishes']  = self.extract(sel,'//div[@class="new-detail-info-sec"][2]/div[5]/div[2]//text()')
				item['website'] = self.extract(sel,'//div[@class="new-detail-info-sec"][3]/div/div[2]//b/text()')

				item['is_reservation_required'] = self.extract(sel,'//ul[@class="micro-property"]/li[1]/@class') or True
				item['is_delivery_service'] = self.extract(sel,'//ul[@class="micro-property"]/li[2]/@class') or True
				item['is_takeaway_service'] = self.extract(sel,'//ul[@class="micro-property"]/li[3]/@class') or True
				item['is_wifi'] =self.extract(sel,'//ul[@class="micro-property"]/li[4]/@class') or True
				item['is_playground_for_kid'] = self.extract(sel,'//ul[@class="micro-property"]/li[5]/@class') or True
				item['is_outdoor_seat'] = self.extract(sel,'//ul[@class="micro-property"]/li[6]/@class') or True
				item['is_private_room'] = self.extract(sel,'//ul[@class="micro-property"]/li[7]/@class') or True
				item['is_air_conditioner'] = self.extract(sel,'//ul[@class="micro-property"]/li[8]/@class') or True
				item['is_credit_card_available'] = self.extract(sel,'//ul[@class="micro-property"]/li[9]/@class') or True
				item['is_karaoke_service'] = self.extract(sel,'//ul[@class="micro-property"]/li[10]/@class') or True
				item['is_free_bike_park'] = self.extract(sel,'//ul[@class="micro-property"]/li[11]/@class') or True
				item['is_tip_for_staff'] = self.extract(sel,'//ul[@class="micro-property"]/li[12]/@class') or True
				item['is_car_park'] = self.extract(sel,'//ul[@class="micro-property"]/li[13]/@class') or True
				item['is_smoking_zone'] = self.extract(sel,'//ul[@class="micro-property"]/li[14]/@class') or True
				item['is_member_card'] = self.extract(sel,'//ul[@class="micro-property"]/li[15]/@class') or True
				item['is_tax_invoice_available'] = self.extract(sel,'//ul[@class="micro-property"]/li[16]/@class') or True
				item['is_conference_support'] = self.extract(sel,'//ul[@class="micro-property"]/li[17]/@class') or True
				item['is_heat_conditioner'] = self.extract(sel,'//ul[@class="micro-property"]/li[18]/@class') or True
				item['is_disabled_person_support'] = self.extract(sel,'//ul[@class="micro-property"]/li[19]/@class') or True
				item['is_live_sport_tv'] = self.extract(sel,'//ul[@class="micro-property"]/li[20]/@class') or True
				item['is_live_music'] = self.extract(sel,'//ul[@class="micro-property"]/li[21]/@class') or True
		except:
			pass

		if item and 'title' in item:
			return item


