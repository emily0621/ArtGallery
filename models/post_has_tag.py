from models.base import Base

from sqlalchemy import Column, Integer, ForeignKey


class PostHasTag(Base):

    __tablename__ = "post_has_tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    post = Column(ForeignKey("post.id"), nullable=False)
    tag = Column(ForeignKey("tag.id"), nullable=False)