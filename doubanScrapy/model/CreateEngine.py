# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Engine:
    def __init__(self):
        pass

    @staticmethod
    def createEng():

        engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/doubandb')
        # 创建DBSession类型:
        session = sessionmaker(bind=engine)
        return session()
