from scrapy.spider import Spider
from scrapy.selector import Selector

from math241.items import Website

class MathSpider(Spider):
    name = "math"
    allowed_domains = ["math.uiuc.edu"]
    start_urls = [
    "http://www.math.uiuc.edu/~schenck/M241S15_files/schedule2.html"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//dl[@class="week"]/dd')
        items = []
# /html/body/dl[1]/dd[2]/text()[4]
        for site in sites:
            item = Website()
            item['name'] = site.xpath('text()[4]').extract()
#            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)

        return items
