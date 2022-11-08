from flask import request
from flask_restx import Resource, Namespace

from project.dao.model.genre import GenreSchema
from project.implemented import genre_service
from project.utils import auth_required, admin_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        res = genre_service.get_all()
        return res, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        r = genre_service.get_item_by_id(gid)
        return r, 200
