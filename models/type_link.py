from models.base import Base

from sqlalchemy import Column, Integer, String


class TypeLink(Base):

    __tablename__ = "type_link"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)
    picture = Column(String(256))
