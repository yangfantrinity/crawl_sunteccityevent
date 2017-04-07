# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 17:08:48 2017

@author: yfan

It is to get the scrapy result 
"""
from twisted.internet import reactor
from scrapy.utils.project import get_project_settings
from scrapy.crawler import Crawler
#from scrapy.settings import Settings
#from scrapy import log, signals
from suntec_events.spiders.suntectevent import suntecevent
from scrapy.xlib.pydispatch import dispatcher

def stop_reactor():
    reactor.stop()

#items = []
#def add_item(item):
#    items.append(item)
#    return items

    
    
dispatcher.connect(stop_reactor, signal=signals.spider_closed)
spider = suntecevent(domain='http://sunteccity.com.sg/events/')
settings = get_project_settings()
crawler = Crawler(spider, settings)
#crawler.configure()
crawler.crawl(spider)
crawler.crawl()
#crawler.signals.connect(add_item, signal=signals.spider_closed)

#log.start()
#log.start(logfile="results.log", loglevel=log.DEBUG, crawler=crawler, logstdout=False)
reactor.run()

reactor.crash()

#with open("results.log", "r") as f:
#    result = f.read()
#print result


## log.start(loglevel=log.DEBUG)
#log.msg("------------>Running reactor")
#result = reactor.run()
#print result
#log.msg("------------>Running stoped")
