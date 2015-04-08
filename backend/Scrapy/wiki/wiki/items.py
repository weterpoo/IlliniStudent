from scrapy.item import Item, Field


class WikiItem(Item):
	name = Field()
	url = Field()
