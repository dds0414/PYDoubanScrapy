# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag_id = scrapy.Field()
    title = scrapy.Field()
    pub = scrapy.Field()
    star = scrapy.Field()
    comment = scrapy.Field()
    desc = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()


class PanScrapyItem(scrapy.Item):
    book_id = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    desc = scrapy.Field()

