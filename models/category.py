from models.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey


class Category(Base):

    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(25), nullable=False)
    category = Column(ForeignKey("category.id"))