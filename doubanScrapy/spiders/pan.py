# -*- coding: utf-8 -*-
import scrapy
from doubanScrapy.items import PanScrapyItem
from bs4 import BeautifulSoup
import re
from doubanScrapy.model.CreateEngine import Engine
from doubanScrapy.model.BookListModel import DbBookList
from scrapy.http import Request
from urllib import unquote
from sqlalchemy import desc


class PanSpider(scrapy.Spider):
    name = "pan"
    allowed_domains = ["wangpansou.cn"]
    baseURL = "http://www.wangpansou.cn"
    start_urls = ()
    # start_urls = (
    #     'http://www.wangpansou.cn/s.php?q=写给大家看的设计书+pdf',
    # )

    def __init__(self):
        super(PanSpider, self).__init__()
        self.session = Engine.createEng()
        d = self.session.query(DbBookList).filter(DbBookList.status == 1).order_by(desc(DbBookList.comment))
        for i in d:
            title = str(i.title.encode("utf8"))
            self.start_urls += ('http://www.wangpansou.cn/s.php?q=%s+pdf&book_id=%s' % (title, i.id),)

    def parse(self, response):
        print response.url
        book_id = re.findall(re.compile('.*?book_id=(.*?)$', re.S), str(response.url))[0]
        data = response.body
        soup = BeautifulSoup(data, 'lxml')
        list_value = soup.find_all('div', 'cse-search-result_content_item')
        for i in list_value:
            item = PanScrapyItem()
            pattern = re.compile('<div.*?href="(.*?)".*?>(.*?)</a>.*?<div.*?>(.*?)</div>', re.S)
            value = re.findall(pattern, str(i))
            item['book_id'] = book_id
            item['title'] = value[0][1].replace('\t', '').replace('\n', '')
            item['href'] = value[0][0]
            item['desc'] = value[0][2].replace('\t', '').replace('\n', '')
            yield item
        # sel = response.xpath("//div[@class='paginator']/a/@href").extract()
        # for s in sel:
        #     # print response.url.split("?")[1].split("&")[0], "->", s.split("?")[1].split("&")[0]
        #     yield Request(self.baseURL + s, callback=self.parse)
