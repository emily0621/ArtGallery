from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import Viewer


class ViewerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Viewer
        exclude = ['id', 'password']
        load_instance = True