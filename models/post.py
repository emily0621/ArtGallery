from models.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey


class Post(Base):

    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(25), nullable=False)
    text = Column(String(1000))
    likes = Column(Integer, nullable=False)
    category = Column(ForeignKey("category.id"), nullable=False)
    url = Column(String(256), nullable=False)
    author = Column(ForeignKey("author.id"), nullable=False)