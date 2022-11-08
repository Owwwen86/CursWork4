import hashlib

import jwt
from flask import request
from flask_restx import abort

from project.constant import PWD_HASH_SALT, PWD_HASH_ITERATIONS


def get_hash(password: str):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ).decode('utf-8', 'ignore')


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            jwt.decode(token, PWD_HASH_SALT, algorithms=['HS256'])
        except Exception:
            print('JWT Decode error')
            abort(401)
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        role = None
        try:
            decode_token = jwt.decode(token, PWD_HASH_SALT, algorithms=['HS256'])
            role = decode_token.get('role')
        except Exception:
            print('JWT Decode error')
            abort(401)
        if role != 'admin':
            abort(403)
        return func(*args, **kwargs)
    return wrapper
