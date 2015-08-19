# -*- coding: utf-8 -*-

from scrapy.http import HtmlResponse
from selenium import webdriver
import time
from scrapy.conf import settings


class JSMiddleware(object):

    # def __init__(self,*args, **kwargs):
    # 	super(JSMiddleware,self).__init__(args,kwargs)

    def process_request(self, request, spider):
	# _d = webdriver.Firefox()	
	_driver = webdriver.Firefox()
        _driver.get(request.url)
        import ipdb; ipdb.set_trace()
        ajax_link = _driver.find_element_by_class_name('btn-load-more').find_element_by_tag_name('a')
        i = 0
        while True:
            # if i > 10 or u"Không tìm thấy kết quả nào" in _driver.page_source:
            #     break
            ajax_link = _driver.find_element_by_class_name('btn-load-more').find_element_by_tag_name('a')
            ajax_link.click()
            i += 1
            time.sleep(3)
        body = _driver.page_source
        _driver.close()
        return HtmlResponse(_driver.current_url, body = body, encoding='utf-8', request = request)
    	# d.close()


