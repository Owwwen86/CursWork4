from flask import request
from flask_restx import Resource, Namespace

from project.dao.model.director import DirectorSchema
from project.implemented import director_service
from project.utils import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_item_by_id(did)

        return director, 200

