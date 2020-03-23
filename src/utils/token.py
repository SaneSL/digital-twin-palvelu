from flask import current_app
import jwt
import datetime


def create_token(id):
    token = jwt.encode({'id': id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'])
    return token