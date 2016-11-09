# -*- coding: utf-8 -*-
import scrapy
from doubanScrapy.items import DoubanscrapyItem
from bs4 import BeautifulSoup
import re
from scrapy.http import Request



class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    baseURL = "https://book.douban.com"
    start_urls = (
        'https://book.douban.com/tag/产品经理?start=0&type=T',
    )
    # rules = [
    #     Rule(SgmlLinkExtractor(allow=(r'/tag/产品经理?start=.*?type=T',)), callback='parse_next_page'),
    # ]

    def parse(self, response):
        # print response

        data = response.body
        soup = BeautifulSoup(data, 'lxml')
        listValue = soup.find_all('li', 'subject-item')
        for i in listValue:
            item = DoubanscrapyItem()
            pattern = re.compile(
                '<li.*?<div class="info">.*?<a.*?>(.*?)</a>.*?<div class="pub">(.*?)</div>.*?<div class="star clearfix">(.*?)</div>(.*?)<div',
                re.S)
            value = re.findall(pattern, str(i))
            p = re.compile('<[^>]+>')
            item['title'] = p.sub("", value[0][0].replace('\n', '').replace(' ', ''))
            item['pub'] = value[0][1].replace('\n', '').strip()
            scValue = p.sub("", value[0][2].replace('\n', '').replace(' ', '').strip()).split("(")
            item['star'] = scValue[0]
            item['comment'] = int(re.findall(r"(\w+)", str(scValue[1]))[0])
            item['desc'] = p.sub("", value[0][3].replace('\n', '').replace(' ', '').strip())
            yield item
            # return item
        sel = response.xpath("//div[@class='paginator']/a/@href").extract()
        for s in sel:
            # print response.url.split("?")[1].split("&")[0], "->", s.split("?")[1].split("&")[0]
            yield Request(self.baseURL + s, callback=self.parse)
