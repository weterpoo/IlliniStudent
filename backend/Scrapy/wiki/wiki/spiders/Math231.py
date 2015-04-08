from scrapy.spider import Spider
from scrapy.selector import Selector
from wiki.items import WikiItem

class Math231Demo(Spider):
	name = "Math231"
	allowed_domains = ["wiki.cites.illinois.edu"]
	start_urls = ["https://wiki.cites.illinois.edu/wiki/display/MATH231Fall2014/Announcements+from+lecture"]
	
	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//div[@class="wiki-content"]/ul/li')
		items = []

		for site in sites:
			item = WikiItem()
			item['name'] = site.xpath('text()').extract()
			items.append(item)
		
		return items
