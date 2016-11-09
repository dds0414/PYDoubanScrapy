# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DbBookList(Base):
    # 表的名字:
    __tablename__ = 'db_book_list'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    pub = Column(String(128))
    star = Column(String(128))
    desc = Column(String(128))


class DoubanscrapyPipeline(object):
    def __init__(self):
        engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/doubandb')
        # 创建DBSession类型:
        session = sessionmaker(bind=engine)
        self.session = session()

    def process_item(self, item, spider):
        # 创建新User对象:
        new_user = DbBookList(title=str(item['title']), pub=str(item['pub']), star=str(item['star']), desc=str(item['desc']))
        # 添加到session:
        self.session.add(new_user)

    def __del__(self):
        # 提交即保存到数据库:
        self.session.commit()
        # 关闭session:
        self.session.close()
