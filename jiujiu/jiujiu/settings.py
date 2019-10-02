# -*- coding: utf-8 -*-

# Scrapy settings for jiujiu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jiujiu'

SPIDER_MODULES = ['jiujiu.spiders']
NEWSPIDER_MODULE = 'jiujiu.spiders'

GENRE = "Young" # Chuanyue, Young, chongshengxiaoshuo, Lsjs

"""
########### SeleniumConfig START ###########
"""
SELENIUM_TIMEOUT = 25           # selenium浏览器的超时时间，单位秒
EXECUTABLE_PATH = "/usr/local/share/"
HEADLESS = True # 浏览器不提供可视化页面

"""
########### SpidersConfig START ###########
"""
# 随机沉睡秒数范围，如果启用了 DOWNLOAD_DELAY，总DELAY时长为 RANDOM_DELAY + DOWNLOAD_DELAY
RANDOM_DELAY = 0

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
REDIRECT_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language':'en-GB,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6,ja;q=0.5,it;q=0.4,el;q=0.3,tr;q=0.2,zh-TW;q=0.1',
    'Cache-Control':'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie':r'xxxxxxxxx这里换成你的cookiexxxxxxxx这里换成你的cookiexxxxxxxxx这里换成你的cookiexxxxxxx',
    'Host': 'www.jjxsw.la',
    'Upgrade-Insecure-Requests': 1,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'jiujiu.middlewares.UserAgentDownloaderMiddleware': 50,
    'jiujiu.middlewares.SeleniumDownloaderMiddleware': 100,
    'jiujiu.middlewares.RandomDelayDownloaderMiddleware': 150,
}