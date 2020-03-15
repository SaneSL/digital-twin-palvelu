import jwt
import datetime
from app import app

def create_token(id):
    token = jwt.encode({'id': id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
    return token