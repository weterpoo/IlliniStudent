from scrapy.spider import Spider
from scrapy.selector import Selector
from wiki.items import WikiItem
import re

class Math241Demo(Spider):
	name = "Math241"
	allowed_domains = ["math.uiuc.edu"]
	start_urls = ["http://www.math.uiuc.edu/~schenck/M241S15_files/schedule2.html#current"]

	def parse(self, response):
		#sel = Selector(None, response.body_as_unicode().replace('\n',''), 'html')
		sel = Selector(response)
		sites = sel.xpath('//dl[@class="week"]/dd')
		items = []

		for site in sites:
			item = WikiItem()
			item['name'] = site.xpath('text()').re(r'HW\s{1}\d+')
			#item['name'] = site.re('HW\s{1}\d+')
			#item['name'] = site.xpath('text()').re(re.match(r'HW\s{1}\w+', re.UNICODE))
			#item['name'] = site.xpath('text()').extract()
			#for i in b:
				#a = i.lower()
				#if "HW" in i:
					#item['name'] = i
			items.append(item)

		return items