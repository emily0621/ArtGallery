from models.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from app import db


class Category(Base):

    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(25), nullable=False)
    category = Column(ForeignKey("category.id"))

    def __init__(self, category_name, category):
        self.category_name = category_name
        self.category = category

    @classmethod
    def getCategoryById(cls, id_category):
        return db.session.query(cls).filter(cls.id == id_category).first()

