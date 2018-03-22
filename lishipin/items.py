# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LishipinItem(scrapy.Item):
    id = scrapy.Field()
    spider = scrapy.Field()
    cate = scrapy.Field()
    title = scrapy.Field()
    keywords = scrapy.Field()
    source = scrapy.Field()
    content = scrapy.Field()
    videoTime = scrapy.Field()
    videoPic = scrapy.Field()
    distincStatu = scrapy.Field()
    smallImgCounts = scrapy.Field()
    smallImgAddr = scrapy.Field()
    imageAddr = scrapy.Field()
    videoAddr = scrapy.Field()
    audioAddr = scrapy.Field()
    audioTime = scrapy.Field()
    comments = scrapy.Field()
    url = scrapy.Field()
    publishTime = scrapy.Field()
    crawledTime = scrapy.Field()