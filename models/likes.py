from models.base import Base

from sqlalchemy import Column, Integer, ForeignKey


class Likes(Base):

    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    viewer = Column(ForeignKey("viewer.id"), nullable=False)
    post = Column(ForeignKey("post.id"), nullable=False)