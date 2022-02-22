from models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

from app import db


class Post(Base):

    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(25), nullable=False)
    text = Column(String(1000))
    likes = Column(Integer, nullable=False)
    category = Column(ForeignKey("category.id"), nullable=False)
    url = Column(String(256), nullable=False)
    author = Column(ForeignKey("author.id"), nullable=False)

    def __init__(self, title, text, category, url, author):
        self.title = title
        self.text = text
        self.category = category
        self.url = url
        self.author = author
        self.likes = 0

    @classmethod
    def getAllPosts(cls):
        return db.session.query(cls).all()
