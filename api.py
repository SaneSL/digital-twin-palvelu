from flask import Flask, jsonify, request, Response, make_response
from app import app
from functools import wraps
from schemas import *
from models import *
import jwt

# Check for json type in all routes


def token_required(func):
    @wraps(func)
    def decorated_functin(*args, **kwargs):
        token = request.json['token']
        
        if token is None:
            body = {'Error': 'Token is missing'}
            return 

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return


# Testing
@app.route('/', methods=['GET'])
def get():
    if request.is_json is False:
        print('Not JSON type, return error')
    return jsonify({'msg': 'Moro'})


# Register
@app.route('/register', methods=['POST'])
def register():
    if request.is_json is False:
        print('Not JSON type, return error')
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
    if request.is_json is False:
        print('Not JSON type, return error')

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
        resp = make_response(r, 400)
        return resp

    username = request.json['username']
    password = request.json['password']

    user = Customer.query.filter(username=username).first()
    if user.password == password:
        return

    user_id = user.id

    results = Result.query.filter(customer_id=user_id, module_id=module_id).first()



