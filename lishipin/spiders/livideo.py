# -*- coding: utf-8 -*-
import re
import scrapy
from copy import deepcopy
import time
from scrapy_redis.spiders import RedisSpider
from py_bloomfilter import PyBloomFilter


class LivideoSpider(RedisSpider):
    """梨视频信息抓取"""
    name = "livideo"
    # allowed_domains = ["pearvideo.com"]
    # start_urls = ['http://www.pearvideo.com/category_loading.jsp?reqType=14&start=12']
    redis_key = "lishipin:start_url"
    bf = PyBloomFilter()

    def parse(self, response):
        item = dict()
        genre = response.url.split('=')[-1]
        cate = {
            "1":"710300", # 社会
            "3":"710500", # 财富(生活)
            "4":"710600", # 娱乐
            "5":"710500", # 生活
            "6":"710500", # 美食(生活)
            "7":"710100", # 搞笑
            "8":"710900", # 科技
            "9":"711000", # 体育
            "17":"711100", # 二次元(动漫)
            "31":"710500", # 汽车(生活)
            "59":"710200", # 音乐
        }
        item["spider"] = "梨视频"
        item["cate"] = cate.get(genre)
        item["videoPic"] = ""
        item["videoAddr"] = ""
        div_list = response.xpath('//div[@class="vervideo-bd"]')
        for i in div_list:
            item["title"] = i.xpath('.//div[@class="vervideo-title"]/text()').extract_first()
            video_num = i.xpath('./a/@href').extract_first()
            video_pic = i.xpath('.//div[@class="verimg-view"]/div/@style').extract_first()
            videoPic = re.findall(r'url\((.*?)\)', video_pic, re.S)
            if videoPic:
                item["videoPic"] = videoPic[0]
            item["smallImgCounts"] = '1'
            item["source"] = i.xpath('.//*[@class="actcont-auto"]/a/text()').extract_first()  # 视频上传人或者推荐人
            playlength = i.xpath('.//div[@class="cm-duration"]/text()').extract_first()
            t = playlength.split(":")
            item["videoTime"] = int(t[0]) * 60 + int(t[1])
            item["comments"] = i.xpath('.//span[@class="fav"]/text()').extract_first()  # 没有评论,这里是收藏数量
            item["url"] = 'http://www.pearvideo.com/'+video_num
            bloom = self.bf.is_exist(item["url"])
            if bloom == 0:  # 没有被爬取过,进行请求
                yield scrapy.Request(item["url"], callback=self.parse_detail, meta={"item": deepcopy(item)})
                self.bf.add(item["url"])

    def parse_detail(self, response):
        item = response.meta['item']
        item["publishTime"] = response.xpath('//div[@class="date"]/text()').extract_first()+':00'
        item["crawledTime"] = str(time.strftime("%Y-%m-%d %X", time.localtime()))
        item["content"] = response.xpath('//div[@class="summary"]/text()').extract_first()
        video_url = re.findall(r'srcUrl="(.*?)"',response.text,re.S)
        item["keywords"] = ""
        item["distincStatu"] = 0
        item["smallImgAddr"] = ""
        item["imageAddr"] = ""
        item["audioAddr"] = ""
        item["audioTime"] = ""
        if video_url:
            item["videoAddr"] = video_url[0]
            yield item