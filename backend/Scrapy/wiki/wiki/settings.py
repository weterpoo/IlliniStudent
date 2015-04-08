# -*- coding: utf-8 -*-

# Scrapy settings for wiki project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'wiki'

SPIDER_MODULES = ['wiki.spiders']
NEWSPIDER_MODULE = 'wiki.spiders'
DEFAULT_ITEM_CLASS = 'wiki.items.WikiItem'

ITEM_PIPELINES = {'wiki.pipelines.WikiPipeline': 0}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wiki (+http://www.yourdomain.com)'
