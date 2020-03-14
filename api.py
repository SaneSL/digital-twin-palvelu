from flask import Flask, jsonify, request, Response, make_response
from app import app
from functools import wraps
from schemas import *
from models import *
import jwt

# Check for json type in all routes


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
            print(request.mimetype)
            print(mimetype)
            if request.mimetype != mimetype:
                value = 'Invalid data type, {} needs to be used'.format(mimetype)
                body = {'Error': value}
                return jsonify(body), 406
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Test
@app.route('/test', methods=['POST'])
@accept()
def testi():
    body = {'succ': 'ess'}
    return jsonify(body)


# Register
@app.route('/register', methods=['POST'])
def register():
    name = request.json['name']
    username = request.json['username']
    password = request.json['password']

    new_Customer = Customer(name=name, username=username, password=password)

    db.session.add(new_Customer)
    db.session.commit()

    return customer_Schema.jsonify(new_Customer)


# Post analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    username = request.json['username']
    password = request.json['password']

    user = Customer.query.filter(username=username).first()
    if user.password == password:
        return

    # Do the module stuff here and return


# Get analysis
@app.route('/analysis/<module_id>', methods=['GET'])
def get_analysis(module_id):
    try:
        module_id = int(module_id)
    except ValueError:
        body = {'Error': 'Invalid parameter'}
        return jsonify(body), 400

    user = Customer.query.filter(username=username).first()
    if user.password == password:
        return

    user_id = user.id

    results = Result.query.filter(customer_id=user_id, module_id=module_id).first()



