# -*- coding: utf-8 -*-
import scrapy
from doubanScrapy.items import DoubanscrapyItem
from bs4 import BeautifulSoup
import re
from scrapy.http import Request
from doubanScrapy.model.CreateEngine import Engine
from doubanScrapy.model.TagNameModel import TagNameModel
import time
from urllib import unquote


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    baseURL = "https://book.douban.com"
    start_urls = ()
    # start_urls = (
    #     'https://book.douban.com/tag/产品经理?start=0&type=T',
    # )

    def __init__(self):
        super(DoubanSpider, self).__init__()
        self.session = Engine.createEng()
        d = self.session.query(TagNameModel).filter(TagNameModel.status == 1).all()
        for i in d:
            self.start_urls += ('https://book.douban.com/tag/%s?start=0&type=T' % i.tag_name,)

    def parse(self, response):
        tag_name = unquote(re.findall(re.compile('.*?tag/(.*?)\?', re.S), str(response.url))[0])
        tag_value = self.session.query(TagNameModel).filter(TagNameModel.tag_name == tag_name).all()
        data = response.body
        soup = BeautifulSoup(data, 'lxml')
        list_value = soup.find_all('li', 'subject-item')
        for i in list_value:
            item = DoubanscrapyItem()
            pattern = re.compile(
                '<li.*?<div class="info">.*?<a.*?>(.*?)</a>.*?<div class="pub">(.*?)</div>.*?<div class="star clearfix">(.*?)</div>(.*?)<div',
                re.S)
            value = re.findall(pattern, str(i))
            p = re.compile('<[^>]+>')
            item['tag_id'] = tag_value[0].id
            item['title'] = p.sub("", value[0][0].replace('\n', '').replace('  ', ''))
            item['pub'] = value[0][1].replace('\n', '').strip()
            scValue = p.sub("", value[0][2].replace('\n', '').replace(' ', '').strip()).split("(")
            item['star'] = scValue[0]
            item['comment'] = int(re.findall(r"(\w+)", str(scValue[1]))[0])
            item['desc'] = p.sub("", value[0][3].replace('\n', '').replace(' ', '').strip())
            item['create_time'] = str(time.time())
            item['update_time'] = str(time.time())
            yield item
        sel = response.xpath("//div[@class='paginator']/a/@href").extract()
        for s in sel:
            # print response.url.split("?")[1].split("&")[0], "->", s.split("?")[1].split("&")[0]
            yield Request(self.baseURL + s, callback=self.parse)
