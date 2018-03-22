# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import redis

from lishipin.settings import REDIS_URL


class LishipinPipeline(object):
    """将视频插入到redis,从reids中弹出item进行下载"""
    def __init__(self):
        self.server = redis.from_url(REDIS_URL)

    def process_item(self, item, spider):
        if spider.name != 'livideo':
            return item
        if item["videoAddr"]:
            self.server.lpush("lishipin:video_items", item)
        return item


class SomePipeline(object):
    """将信息保存到txt"""
    def process_item(self, item, spider):
        with open('梨视频下载.txt','a') as f:
            json.dump(item,f,ensure_ascii=False,indent=2)
        return item



