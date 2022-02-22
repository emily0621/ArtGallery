from app import db
from models import Viewer
from datetime import datetime


def viewerInsert():
    db.session.add(Viewer(
        username='user1',
        email='user1@mail.com',
        password='user1_password',
        avatar_link='link1',
        date_of_birth=datetime(2001, 1, 2)
    ))
    db.session.add(Viewer(
        username='user2',
        email='user2@mail.com',
        password='user2_password',
        avatar_link='link2',
        date_of_birth=datetime(2001, 1, 2)
    ))
    db.session.add(Viewer(
        username='user3',
        email='user3@mail.com',
        password='user3_password',
        avatar_link='link3',
        date_of_birth=datetime(2001, 1, 2)
    ))
    db.session.commit()

