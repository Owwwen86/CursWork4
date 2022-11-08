from flask import request
from flask_restx import Resource, Namespace, abort

from project.dao.model.user import UserSchema
from project.implemented import user_service
from project.implemented import auth_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        res = UserSchema(many=True).dump(users)
        return res, 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        res = UserSchema().dump(user)
        return res, 200

    def patch(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.patch(req_json)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204


@user_ns.route('/<int:uid>/password/')
class UserChangePassword(Resource):
    def put(self, uid):
        req_json = request.json

        password_1 = req_json.get('password_1')
        password_2 = req_json.get('password_2')

        if not password_1 or not password_2:
            abort(400)

        user = user_service.get_one(uid)
        password_1 = auth_service.get_hash(password_1)
        if password_1 != user.password:
            return {"error": "Пароль неверный"}, 401

        user.password = auth_service.get_hash(password_2)

        user_service.update_password(user)
