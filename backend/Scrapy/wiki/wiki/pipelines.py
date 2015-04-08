# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class WikiPipeline(object):

	words_to_filter = ['due']

	def process_item(self, item, spider):
		for word in self.words_to_filter:
			if not word in unicode(item['name']).lower():
				raise DropItem("Not related string: %s" % word)
		else:
			return item