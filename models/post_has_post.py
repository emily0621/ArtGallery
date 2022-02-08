from models.base import Base

from sqlalchemy import Column, Integer, ForeignKey


class PostHasPost(Base):

    __tablename__ = "post_has_post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_first = Column(ForeignKey("post.id"), nullable=False)
    post_second = Column(ForeignKey("post.id"), nullable=False)