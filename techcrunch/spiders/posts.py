# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
from scrapy.http import Request
from scrapy.selector import Selector

class PostsSpider(scrapy.Spider):
    name = "posts"
    allowed_domains = ["techcrunch.com"]
    start_urls = ['https://techcrunch.com/']
    # Generate list of the pages 
    for page in range(2,202):
    	start_urls.append('https://'+allowed_domains[0]+'/page/'+str(page)+'/')

    def parse(self, response):
	sel = Selector(response)
	# Getting from news blocks data 
        cams = sel.css('div.block-thumb')
        for cam in cams:
	    yield {
            'time': cam.css('div.byline time::attr(datetime)').extract_first(),
	    'title': cam.css('h2.post-title a::text').extract_first(),
            'author': cam.css('a[rel="author"]::text').extract_first(),
	    'tag': cam.css('a.tag span::text').extract_first(),
	}


