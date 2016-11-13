# -*- coding: utf-8 -*-
import time
from model.BookListModel import DbBookList
from model.TagNameModel import TagNameModel
from model.PanListModel import PanListModel
from model.CreateEngine import Engine


class ScrapyPipeline(object):
    def __init__(self):
        self.session = Engine.createEng()

    def process_item(self, item, spider):
        if spider.name == "douban":
            self.douban_pipeline(item)
        elif spider.name == "pan":
            self.pan_pipeline(item)
        self.session.commit()

    def douban_pipeline(self, item):
        # 创建新User对象:
        new_user = DbBookList(tag_id=str(item['tag_id']), title=str(item['title']).strip(), pub=str(item['pub']), star=str(item['star']), comment=str(item['comment']), desc=str(item['desc']), update_time=time.time())
        d = self.session.query(DbBookList).filter(DbBookList.tag_id == new_user.tag_id).filter(
            DbBookList.title == new_user.title).all()
        if len(d) > 0:
            self.session.query(DbBookList).filter(DbBookList.tag_id == new_user.tag_id).filter(
                DbBookList.title == new_user.title).update({
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
        self.session.query(TagNameModel).filter(TagNameModel.id == new_user.tag_id).update({
            TagNameModel.status: 0})

    def pan_pipeline(self, item):
        new_pan = PanListModel(book_id=item['book_id'], title=item['title'], href=item['href'], desc=item['desc'])
        self.session.add(new_pan)

    def __del__(self):
        # 关闭session:
        self.session.close()
