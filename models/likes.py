from models.base import Base

from sqlalchemy import Column, Integer, ForeignKey
from app import db


class Likes(Base):

    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    viewer = Column(ForeignKey("viewer.id"), nullable=False)
    post = Column(ForeignKey("post.id"), nullable=False)

    @classmethod
    def deleteLikeByPostId(cls, post_id):
        db.session.query(cls).filter(cls.post == post_id).delete()
        db.session.commit()
