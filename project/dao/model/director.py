from marshmallow import Schema, fields

from project.setup import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)


class DirectorSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
