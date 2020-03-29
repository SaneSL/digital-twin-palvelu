from flask import current_app
import jwt
import datetime


def create_token(id):
    print(current_app.config['SECRET_KEY'])
    token = jwt.encode({'id': id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'])
    return token.decode('utf-8')