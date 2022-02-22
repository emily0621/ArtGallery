from app import db
from models import Post


def postInsert():
    db.session.add(Post(
        title='post1',
        text='my new post1',
        category=2,
        url='picture_url',
        author=1
    ))
    db.session.commit()