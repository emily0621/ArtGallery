from models.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey


class LinksForAuthor(Base):

    __tablename__ = "links_for_author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String(25), nullable=False)
    type_link = Column(ForeignKey("type_link.id"), nullable=False)
    author = Column(ForeignKey("author.id"), nullable=False)