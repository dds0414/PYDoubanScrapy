# -*- coding: utf-8 -*-
from BaseModel import Base
from sqlalchemy import Column, String, create_engine, Integer


class DbBookList(Base):
    # 表的名字:
    __tablename__ = 'db_book_list'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    tag_id = Column(String(20))
    title = Column(String(20))
    pub = Column(String(128))
    star = Column(String(128))
    comment = Column(String(128))
    desc = Column(String(128))
    create_time = Column(String(128))
    update_time = Column(String(128))
    status = Column(String(128))
