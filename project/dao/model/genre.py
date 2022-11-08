from marshmallow import Schema, fields

from project.setup import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)


class GenreSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
