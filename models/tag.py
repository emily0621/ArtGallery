from models.base import Base

from sqlalchemy import Column, Integer, String


class Tag(Base):

    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(String(25), nullable=False)