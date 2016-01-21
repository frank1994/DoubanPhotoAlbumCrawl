豆瓣相册爬虫

===================

### 简介
爬取豆瓣相册中的图片。基于 Python+scrapy 编写。

![student](http://7xi5vu.com1.z0.glb.clouddn.com/2016-01-21-readmestudent.png?imageView/2/w/619/q/90)

![hungry](http://7xi5vu.com1.z0.glb.clouddn.com/2016-01-21-readmehungry.png?imageView/2/w/619/q/90)  
![wahaha](http://7xi5vu.com1.z0.glb.clouddn.com/2016-01-21-readmefinder_image.png?imageView/2/w/619/q/90)

再推荐一个豆列吧：[传说中的表情包](http://www.douban.com/doulist/35796198/)
还等什么，一起来玩吧，hiahiahia

### 运行环境：
* Linux | Mac OS
* python 版本为2.7.x
* scrapy 1.0.4

### 使用方法：

#### 1. 写入链接
1. 将相册的地址写入`./DownloadImage/DownloadImage/spiders`的`LinkList.txt`中，写入后保存，每一行写一个相册链接。

2. 修改后保存。

#### 2. 运行

```
cd ./DownloadImage
scrapy crawl downloadspider
```

运行完毕后，图片保存在`./DownloadImage/DownloadImage/Image`

###后期改进：
- [x] 自动检测相册页数
- [ ] 按相册分类建文件夹存放图片
- [ ] 支持豆列形式的地址，即 https://www.douban.com/doulist/...形式的地址
- [ ] 支持电影剧照，即 https://movie.douban.com/photos/photo/...形式的地址
- []  ...