from app import db
from models import Category


def categoryInsert():
    db.session.add(Category(
        category_name='category1',
        category=None
    ))
    db.session.commit()
    db.session.add(Category(
        category_name='category2',
        category=1
    ))
    db.session.commit()