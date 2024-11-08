import os 
import logging
import scrapy
from scrapy.crawler import CrawlerProcess



class BookingSpider(scrapy.spider):
  name = "booking"

  start_urls = ["https://www.booking.com/"]

  def parse(self, response):
    


