from sqlalchemy import MetaData, Column, Integer, String, Boolean, Text
from sqlalchemy.orm import declarative_base

metadata = MetaData()
Base = declarative_base()


# todo добавить популярность товара
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
