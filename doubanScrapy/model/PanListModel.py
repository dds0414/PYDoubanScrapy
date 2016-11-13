# -*- coding: utf-8 -*-
from doubanScrapy.model.BaseModel import Base
from sqlalchemy import Column, String, create_engine, Integer


class PanListModel(Base):
    # 表的名字:
    __tablename__ = 'db_pan_list'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    book_id = Column(String(128))
    title = Column(String(128))
    href = Column(String(128))
    desc = Column(String(128))

