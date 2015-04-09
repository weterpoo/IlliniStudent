# -*- coding: utf-8 -*-

# Scrapy settings for math241 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'math241'

SPIDER_MODULES = ['math241.spiders']
NEWSPIDER_MODULE = 'math241.spiders'
DEFAULT_ITEM_CLASS = 'math241.items.mathItem'

ITEM_PIPELINES = {'math241.pipelines.Math241Pipeline':1}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'math241 (+http://www.yourdomain.com)'
