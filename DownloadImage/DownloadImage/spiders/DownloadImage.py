# -*- coding: utf-8 -*-

import os
import re
import urllib2

from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request


class GetUrlSpider(BaseSpider):
    name = "downloadspider"
    allowed_domains = ["douban.com", "doubanio.com"]
    download_delay = 0.2
    counter = 0
    try:
        base_path = unicode(os.path.abspath('.').decode('gbk'))  # 初始地址,不含分隔符
    except:
        base_path = os.path.abspath('.')  # 对于Mac和Linux用户，使用gbk解码反而会造成崩溃，故添加一个try-except，以防万一

    if not os.path.exists(base_path + '/Image'):
        os.mkdir(base_path + '/Image')
    print u"开始读取LinkList.txt的内容"
    with open(base_path + '/DownloadImage/spiders/LinkList.txt', 'r') as link_list:
        album_id_page_list = []
        for line in link_list:
            line = line.replace(' ', '').replace('\r', '').replace('\n', '').replace('\t', '')  # 移除空白字符
            album_id_re = re.search(r'(?<=/)\d+(?=/)', line)
            if album_id_re is not None:
                album_id_single = int(album_id_re.group(0))
                # print "album_id_single????:" + str(album_id_single)

                objResponse = urllib2.urlopen(line)
                strResponse = objResponse.read()
                objResponse.close()
                page_num_re = re.search(r'(?<=<span class="count">\(共).*?(?=张\)</span>)', strResponse)
                if page_num_re is not None:
                    page_num = int(page_num_re.group(0))/18 + 1
                else:
                    page_num = 1      # 如果没有"共*张"的字符串,那么默认是一页
                # print "page_num" + str(page_num)
                album_id_page_list.append([album_id_single, page_num])
            else:
                print "Error!!!"
            counter += 1

    start_urls = []
    for [album, page] in album_id_page_list:
        for i in range(0, 18*page, 18):
            start_urls.append('http://douban.com/photos/album/%d/?start=%d' % (album, i))

    def parse(self, response):
        print response
        hxs = HtmlXPathSelector(response)
        req = []
        # sites = hxs.select("//ul/li/div[@class='cover']/a/img/@src").extract()
        sites = hxs.select("//div[@class='photo_wrap']/a/img/@src").extract()
        print sites
        for site in sites:
            print site
            site = site.replace('thumb', 'photo')
            r = Request(site, callback=self.DownLload)
            req.append(r)
        return req

    def DownLload(self, response):
        str = response.url[0:-3]
        self.counter += 1
        str = str.split('/')
        # print '----------------Image Get----------------', self.counter, str[-1], 'jpg'
        img_file = open(self.base_path+'/Image/'+str[-1]+"jpg", 'wb')
        img_file.write(response.body)
        img_file.close()
        return