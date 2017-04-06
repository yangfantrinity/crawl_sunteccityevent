# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 09:52:08 2017

@author: yfan

It is the web crawler to get the event information on Suntec event webpage
"""

#import csv
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from suntec_events.items import SuntecEventsItem

class suntecevent(BaseSpider):
    name = 'sunteceventcrawler'
    allowed_domains = ["sunteccity.com.sg"]
    start_urls = ["http://sunteccity.com.sg/events/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
#        print response
        titles = hxs.xpath("//div[@class='column-4 dealtxt']")
#        print titles
        items = []
        for i in range(len(titles)):
            title = titles[i]
            item = SuntecEventsItem()
            item['event_name'] = title.select("div[1]/div/span/text()").extract()
            item['event_time'] = title.select("div[3]/p[1]/span/text()").extract()
            item['event_location'] = title.select("div[3]/p[3]/text()").extract()
            items.append(item)
            print item
        return items
