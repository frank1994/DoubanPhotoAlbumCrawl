# coding:utf-8

# ###################################################################
# Description:      输入网址后自动只看楼主并保存到本地文件
#                       将楼主发布的页面下载并存储到本地文件夹。
# Author:           Frank
# Date:             2015.01.28
# Version:          0.1
# ###################################################################

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import os

class GetUrlSpider(BaseSpider):
    name = "downloadspider"
    allowed_domains = ["douban.com"]
    download_delay = 0.2
    counter = 0;
    if not os.path.exists('./Image'):
        os.mkdir('./Image')

    albumId = [[71097918,18]]
    start_urls = [];
    for [album,page] in albumId:
        for i in range(0,18*(page+1),18):
                start_urls.append('http://douban.com/photos/album/%d/?start=%d' % (album,i))

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        req = []
        # sites = hxs.select("//ul/li/div[@class='cover']/a/img/@src").extract()
        sites = hxs.select("//div[@class='photo_wrap']/a/img/@src").extract()
        for site in sites:
            print site
            site = site.replace('thumb','photo')
            r = Request(site, callback=self.DownLload)
            req.append(r)
        return req

    def DownLload(self, response):
        str = response.url[0:-3];
        self.counter = self.counter+1
        str = str.split('/');
        print '----------------Image Get----------------',self.counter,str[-1],'jpg'
        imgfile = open('./Image/'+str[-1]+"jpg",'wb')
        imgfile.write(response.body)
        imgfile.close()
