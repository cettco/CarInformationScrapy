# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TorrentItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    sid = scrapy.Field()
    font_score = scrapy.Field()
    koubei_con=scrapy.Field()
    koubei_rival=scrapy.Field()
class IdItem(scrapy.Item):
	id=scrapy.Field()

class TencentItem(scrapy.Item):
	name=scrapy.Field()
	sid=scrapy.Field()
	comment=scrapy.Field()

class XcarItem(scrapy.Item):
	name=scrapy.Field()
	sid=scrapy.Field()
	comment=scrapy.Field()

