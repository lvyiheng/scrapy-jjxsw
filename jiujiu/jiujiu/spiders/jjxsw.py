# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jiujiu.settings import *


class JjxswSpider(CrawlSpider):
    name = 'jjxsw'
    allowed_domains = ['www.jjxsw.la']
    start_urls = ['https://www.jjxsw.la/txt/{}/'.format(GENRE)]

    rules = (
        Rule(LinkExtractor(allow=r'.+/txt/{}[/index_]*[\d+]*\.html'.format(GENRE)), callback='parse_page', follow=True), # 跳页
        # Rule(LinkExtractor(allow=r'.+/txt/{}/index_2\.html'.format(GENRE)), callback='parse_page', follow=True), # 跳页
    )

    def parse_page(self, response):
        book_list = response.xpath(""".//*[@id="catalog"]//div/span[contains(text(), "荐")]/../a""")
        for book in book_list:
            href = book.xpath("""@href""").extract()[0]
            title = book.xpath("""@title""").extract()[0]
            url = "https://www.jjxsw.la" + href
            yield scrapy.Request(url=url, callback=self.parse_item, meta={'book_title': title}, dont_filter=True)


    def parse_item(self, response):
        title = response.meta['book_title']
        download_href = response.xpath("""//*[@id="mainstory"]/ul[1]/li[1]/a/@href""").extract()[0]
        url = "https://www.jjxsw.la" + download_href
        yield scrapy.Request(url=url, meta={'book_title': title}, dont_filter=True)