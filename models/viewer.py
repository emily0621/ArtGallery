from models.base import Base

from sqlalchemy import Column, Integer, String, Date


class Viewer(Base):

    __tablename__ = "viewer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(25), unique=True, nullable=False)
    email = Column(String(25), unique=True, nullable=False)
    password = Column(String(45), nullable=False)
    avatar_link = Column(String(256))
    date_of_birth = Column(Date, nullable=False)


