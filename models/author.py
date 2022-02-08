from models.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey


class Author(Base):

    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    watermark = Column(String(256), unique=True, nullable=False)
    first_name = Column(String(25))
    last_name = Column(String(25))
    phone = Column(String(25))
    viewer_id = Column(ForeignKey('viewer.id'), nullable=False)
    country = Column(String(25))
    city = Column(String(25))
