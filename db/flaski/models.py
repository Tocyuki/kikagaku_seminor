# coding: utf-8
from sqlalchemy import Column, Integer, String, Float
from flaski.database import Base
from datetime import datetime

class Chart(Base):
    __tablename__ = 'charts'
    id    = Column(Integer, primary_key=True)
    label = Column(String(20))
    value = Column(Float)

    def __init__(self, label=None, value=None):
        self.label = label
        self.value = value
