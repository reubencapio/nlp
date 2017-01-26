from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.spiders import BaseSpider
import scrapy
from bs4 import BeautifulSoup
import urllib
import re
import sys 
sys.path.append('D:\downloads\depot_tools\depot_tools\python276_bin\Lib\site-packages')
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
import html2text


class someSpider(CrawlSpider):
	name = 'crawltest2'
	allowed_domains = ['news.abs-cbn.com']
	start_urls = ['http://news.abs-cbn.com/']
	
	rules = (Rule (LinkExtractor(), callback="parse_obj", follow=True),)

	def parse_obj(self, response):
		print "respone.url == " + response.url
		filename = response.url	
		filename = re.sub(r'[\W_]+', '', filename)
		filename = filename.translate(None, ':/') + '.txt'
		filename = 'C:/Users/FPT Software/scraper/tutorial/tutorial/spiders/output/' + filename;
		#print "filename == " + filename	

		
		with open(filename, 'wb') as f:
			soup = BeautifulSoup(response.body, "html5lib")
			text = [p.get_text() for p in soup.find_all('p')]
			output = ''.join(text)
			if not output:
				print "blankline"
			else:
				f.write(output.encode('utf-8'))