# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from jiujiu.settings import *
from jiujiu.useragent import USER_AGENT
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import logging
import platform


class UserAgentDownloaderMiddleware(object):

    def __init__(self, user_agent=USER_AGENT):
        self.USER_AGENT = user_agent

    def process_request(self, request, spider):
        request.headers.setdefault(b"User-Agent", random.choice(self.USER_AGENT))


class RandomDelayDownloaderMiddleware(object):
    def __init__(self):
        self.delay = RANDOM_DELAY

    def process_request(self, request, spider):
        delay = random.randint(0, self.delay)
        logging.debug("### random delay: %s s ###" % delay)
        time.sleep(delay)


class SeleniumDownloaderMiddleware(object):
    def __init__(self):
        self.timeout = SELENIUM_TIMEOUT
        self.executable_path = EXECUTABLE_PATH
        chrome_options = webdriver.ChromeOptions()
        if HEADLESS:
            chrome_options.add_argument('--headless')
        if platform.system() == 'Windows':
            self.browser = webdriver.Chrome(executable_path=self.executable_path, chrome_options=chrome_options)
        else:
            chrome_options.add_argument('no-sandbox')  # 针对linux root用户
            self.browser = webdriver.Chrome(chrome_options=chrome_options)

        self.browser.maximize_window()
        self.browser.set_page_load_timeout(self.timeout)
        self.browser.implicitly_wait(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def process_request(self, request, spider):
        # 指定需要 selenium 处理的下载情况
        if "https://www.jjxsw.la/txt/dl" in request.url:
            title = request.meta['book_title']
            self.browser.get(request.url)
            self.browser.find_element_by_xpath('//*[@id="Frame"]//a[contains(text(), "TXT电子书下载地址")]').click()
            logging.info("{} is downloading...".format(title))

    def close_spider(self, spider):
        self.browser.quit()
