from app import db
from models import Author


def authorInsert():
    db.session.add(Author(
        watermark='watermark1',
        first_name='first_name1',
        last_name='last_name1',
        phone='11234',
        viewer_id=1,
        country='Ukraine',
        city='Lviv'
    ))
    db.session.commit()

