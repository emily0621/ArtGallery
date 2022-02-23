from models.base import Base
from models.author import Author
from models.viewer import Viewer
from models.likes import Likes
from models.comments import Comments
from models.post_has_tag import PostHasTag
from models.category import Category
from sqlalchemy import Column, Integer, String, ForeignKey

from app import db


class Post(Base):

    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(25), nullable=False)
    text = Column(String(1000))
    likes = Column(Integer, nullable=False)
    category = Column(ForeignKey("category.id"), nullable=False)
    url = Column(String(256), nullable=False)
    author = Column(ForeignKey("author.id"), nullable=False)

    def __init__(self, title, text, category, url, author):
        self.title = title
        self.text = text
        self.category = category
        self.url = url
        self.author = author
        self.likes = 0

    @staticmethod
    def addPost(title, text, category, url, author):
        if len(title) > 25:
            return 'Long title'
        if len(text) > 1000:
            return 'Long text'
        if Category.getCategoryById(category) is None:
            return 'Category doesn`t exists'
        post = Post(
            title=title,
            text=text,
            category=category,
            url=url,
            author=author
        )
        db.session.add(post)
        db.session.commit()
        return post

    def setTitle(self, title):
        if len(title) > 25:
            return False
        self.title = title
        return True

    def setText(self, text):
        if len(text) > 1000:
            return False
        self.text = text
        return True

    def setCategory(self, category):
        if Category.getCategoryById(category) is None:
            return False
        self.category = category
        return True

    @staticmethod
    def commit():
        db.session.commit()

    @classmethod
    def getAllPosts(cls):
        return db.session.query(cls).all()

    @classmethod
    def getAllPostsByAuthor(cls, username):
        author = Author.getAuthorByUsername(username)
        if not author:
            return False
        return db.session.query(cls).filter(cls.author == author.id)

    @classmethod
    def getPostById(cls, id_post):
        return db.session.query(cls).filter(cls.id == id_post).first()

    @classmethod
    def deletePostById(cls, id_post):
        if not cls.getPostById(id_post):
            return False
        Likes.deleteLikeByPostId(id_post)
        Comments.deleteCommentByPostId(id_post)
        PostHasTag.deletePostHasTagByPostId(id_post)
        db.session.delete(db.session.query(cls).filter(cls.id == id_post).first())
        db.session.commit()
        return True
