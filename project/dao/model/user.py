from marshmallow import Schema, fields

from project.setup import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    favorite_genre = db.Column(db.String(150))


class UserSchema(Schema):
    id = fields.Str(required=True)
    email = fields.Str(required=True)
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()