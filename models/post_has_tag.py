from models.base import Base

from sqlalchemy import Column, Integer, ForeignKey
from app import db


class PostHasTag(Base):

    __tablename__ = "post_has_tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    post = Column(ForeignKey("post.id"), nullable=False)
    tag = Column(ForeignKey("tag.id"), nullable=False)

    @classmethod
    def deletePostHasTagByPostId(cls, post_id):
        db.session.query(cls).filter(cls.post == post_id).delete()
        db.session.commit()
