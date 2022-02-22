from marshmallow import Schema, fields


class FullPostSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    text = fields.String()
    likes = fields.Integer()
    category = fields.Integer()
    url = fields.String()
    author = fields.Integer()


class WithoutIdPostSchema(Schema):
    title = fields.String()
    text = fields.String()
    likes = fields.Integer()
    category = fields.Integer()
    url = fields.String()
    author = fields.Integer()
