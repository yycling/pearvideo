#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: cling

import redis
from lishipin.settings import REDIS_URL


class StartLiShiPin(object):
    def __init__(self):
        self.server = redis.from_url(REDIS_URL)

    def lishipin_url(self):
        urls = []
        for i in [1, 3, 4, 5, 6, 7, 8, 9, 17, 31, 59]:
            zixun_url = ['http://www.pearvideo.com/category_loading.jsp?reqType=5&start={}&categoryId={}'.format(j * 12, i)
                for j in range(1)]
            urls.extend(zixun_url)
        paike_url = ['http://www.pearvideo.com/category_loading.jsp?reqType=14&start={}&categoryId=5'.format(i * 12) for
                     i in range(1)]  # 拍客短视频
        urls.extend(paike_url)

        for url in urls:
            self.server.rpush("lishipin:start_url", url)

if __name__ == '__main__':
    StartLiShiPin().lishipin_url()

