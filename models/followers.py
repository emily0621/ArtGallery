from models.base import Base

from sqlalchemy import Column, Integer, ForeignKey


class Followers(Base):

    __tablename__ = "followers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(ForeignKey("author.id"), nullable=False)
    viewer = Column(ForeignKey("viewer.id"), nullable=False)
