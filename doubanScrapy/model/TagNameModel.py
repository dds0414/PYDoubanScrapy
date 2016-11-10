# -*- coding: utf-8 -*-
from BaseModel import Base
from sqlalchemy import Column, String, Integer, DateTime


class TagNameModel(Base):
    # 表的名字:
    __tablename__ = 'db_tag_list'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(255))
    create_time = Column(DateTime())
    update_time = Column(DateTime())
    status = Column(Integer)

