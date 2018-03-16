import scrapy
import os
import datetime

class TestSpider(scrapy.Spider):
	name = "download_stocksdata"

	start_urls = [
		"http://www.pesobility.com/stock",
		"http://wsj.com/mdc/public/page/9_3024-AsianStocks_MANILA.html",
	]

	def parse(self, response):
		filename = response.url.split("/")[-1] + '.html'
		now = datetime.datetime.now()
		now = str(now)
		now = now.split(' ')
		now = now[0]
		
		newpath = r'C:/news_data_for_nlp_' + now + '/'
		if not os.path.exists(newpath):
			os.makedirs(newpath)
			
		filename = newpath + '/' + filename;
			
		with open(filename, 'wb') as f:
			f.write(response.body)