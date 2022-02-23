from models.base import Base
from models.viewer import Viewer

from sqlalchemy import Column, Integer, String, ForeignKey
from app import db

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

    def __init__(self, watermark, first_name, last_name, phone, viewer_id, country, city):
        self.watermark = watermark
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.viewer_id = viewer_id
        self.country = country
        self.city = city

    @classmethod
    def getAuthorByUsername(cls, username):
        viewer = Viewer.getViewerByUsername(username)
        if not viewer:
            return False
        author = db.session.query(cls).filter(cls.viewer_id == viewer.id).first()
        if not author:
            return False
        return author
