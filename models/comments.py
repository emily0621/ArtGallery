from models.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from app import db


class Comments(Base):

    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(256), nullable=False)
    likes = Column(Integer, nullable=False)
    post = Column(ForeignKey("post.id"), nullable=False)
    viewer = Column(ForeignKey("viewer.id"), nullable=False)

    @classmethod
    def deleteCommentByPostId(cls, post_id):
        db.session.query(cls).filter(cls.post == post_id).delete()
        db.session.commit()
