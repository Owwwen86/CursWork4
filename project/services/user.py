from project.dao.user import UserDAO
from project.utils import get_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        user_d['password'] = get_hash(user_d['password'])
        return self.dao.create(user_d)

    def patch(self, data):
        user = self.get_one(data['id'])

        if data.get('name'):
            user.name = data['name']
        if data.get('surname'):
            user.surname = data['surname']
        if data.get('favorite_genre'):
            user.favorite_genre = data['favorite_genre']

        self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)

    def update_password(self, data):
        self.dao.update(data)
