# -*- coding: utf-8 -*-
import scrapy
from ..items import MimiItem


class FcSpider(scrapy.Spider):
    name = 'FC'
    #allowed_domains = ['pastpapersz.com/']
    start_urls = ['http://www.pastpapersz.com/edexcel/igcse-mathematics-b/']

    def parse(self, response):
      items = MimiItem()
      divs = response.css('div.one_half')
      for div in divs:
       year = div.css('h4::text').extract()
       link = div.css( 'a').xpath('@href').extract()

       items['year'] = year
       #items['papers']= paper
       #items['session'] = session
       items['link'] = link
       yield items
