from functools import wraps
from flask import Flask, jsonify, request, Response, make_response, current_app
import jwt

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.json.get('token', None)
        if token is None:
            body = {'error': 'Token is missing'}
            return jsonify(body), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user_id = data.get('id', None)
        except:
            body = {'error': 'Token is invalid'}
            return jsonify(body), 403
        return func(user_id, *args, **kwargs)
    return wrapper


def accept(mimetype='application/json'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.mimetype != mimetype:
                value = 'Invalid data type, {} needs to be used'.format(mimetype)
                body = {'error': value}
                return jsonify(body), 406
            return func(*args, **kwargs)
        return wrapper
    return decorator