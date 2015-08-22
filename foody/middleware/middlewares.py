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

