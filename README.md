豆瓣相册爬虫

===================

###运行环境：
* Ubuntu14.04 | Mac OS
* python版本为2.7x
* scrapy

###使用方法：

####1.设置要下载的页面id和页数:
修改`...\douban-image-scrapy\DownloadImage\DownloadImage\spiders`的`DownloadImage.py`,找到`albumId = [....]`
第一个值是相册的id，第二个值是相册的页数。例如：

```
albumId = [[139011725,13]]
```
修改后保存即可

####2.运行

```
cd .\DownloadImage
scrapy crawl downloadspider
```

运行完毕后，图片保存在`...\douban-image-scrapy\DownloadImage\Image`

###后期改进：
* 自动检测相册页数
* 按相册分类建文件夹存放图片
