# -*- coding: utf-8 -*-

from scrapy.http import HtmlResponse, Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from scrapy.conf import settings
import re
import random


from scrapy.conf import settings

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')

class RandomUserAgentMiddleware(object):
    def process_request(self, request,spider):
        userAgent = random.choice(settings.get('USER_AGENT_LIST'))
        if userAgent:
            request.headers.setdefault("User-Agent", userAgent)

class JSMiddleware(object):

    def __init__(self,*args, **kwargs):
    	super(JSMiddleware,self).__init__(*args, **kwargs)
        self.dcap = dict(DesiredCapabilities.PHANTOMJS)
        self.dcap["phantomjs.page.settings.userAgent"] = random.choice(settings.get('USER_AGENT_LIST'))

    def process_request(self, request, spider):
	_driver = webdriver.PhantomJS(desired_capabilities=self.dcap)
        _driver.set_window_size(1440, 900)
        _driver.set_page_load_timeout(180)
        _driver.get(request.url)
        i = 0
        while i < 15:
            ajax_link = None
            try:
               # if 'http://www.foody.vn/bo-suu-tap/' in request.url:
               #    import ipdb; ipdb.set_trace()
               #    pass
               ajax_link = _driver.find_element_by_class_name('lists-btn-load-more')
            except:
               if 'http://www.foody.vn/bo-suu-tap/' not in request.url:
                   ajax_link = _driver.find_element_by_class_name('btn-load-more').find_element_by_tag_name('a')
            finally:
               i += 1
               if ajax_link:
                   ajax_link.click()
                   time.sleep(3)
        body = _driver.page_source
        url = _driver.current_url
        _driver.close()
        return HtmlResponse(url, body = body, encoding='utf-8', request = request)
        # return HtmlResponse(request.url, encoding='utf-8', request = request)
