# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from model.BookListModel import DbBookList
from model.CreateEngine import Engine


class DoubanscrapyPipeline(object):
    def __init__(self):
        self.session = Engine.createEng()

    def process_item(self, item, spider):
        # 创建新User对象:
        new_user = DbBookList(tag_id=str(item['tag_id']),title=str(item['title']), pub=str(item['pub']), star=str(item['star']),comment=str(item['comment']), desc=str(item['desc']), update_time=time.time())
        d = self.session.query(DbBookList).filter(DbBookList.title == new_user.title).all()
        if len(d) > 0:
            self.session.query(DbBookList).filter(DbBookList.title == new_user.title).update({
                DbBookList.tag_id: new_user.tag_id,
                DbBookList.title: new_user.title,
                DbBookList.pub: new_user.pub,
                DbBookList.star: new_user.star,
                DbBookList.comment: new_user.comment,
                DbBookList.desc: new_user.desc,
                DbBookList.update_time: new_user.update_time
            })
        else:
            # 添加到session:
            new_user.create_time = item['create_time']
            self.session.add(new_user)
        # 提交即保存到数据库:
        self.session.commit()

    def __del__(self):
        # 关闭session:
        self.session.close()
