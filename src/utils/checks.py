from functools import wraps
from flask import Flask, jsonify, request, Response, make_response
import jwt

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.json['token']
        
        if token is None:
            body = {'Error': 'Token is missing'}
            return jsonify(body), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            body = {'Error': 'Token is invalid'}
            return jsonify(body), 403

        return func(*args, **kwargs)
    return decorated_function(*args, **kwargs)


def accept(mimetype='application/json'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.mimetype != mimetype:
                value = 'Invalid data type, {} needs to be used'.format(mimetype)
                body = {'Error': value}
                return jsonify(body), 406
            return func(*args, **kwargs)
        return wrapper
    return decorator