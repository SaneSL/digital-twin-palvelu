from flask import Flask, jsonify, request, Response, make_response, render_template
from app import app
from uuid import uuid4
from utils.checks import *
from utils.exceptions import *
from utils.token import create_token
from schemas import *
from models import *
import jwt, datetime

# TODO:
# Min/max lenght for password and username
# Catch database errors



@app.errorhandler(DatabaseError)
@app.errorhandler(ApiAuthenticationError)
@app.errorhandler(ArgMissingError)
def handle_it(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Test
@app.route('/')
def testi():
    raise DatabaseError


# Test 2
@app.route('/home')
def home():
    return render_template('home.html')


# Register
@app.route('/register', methods=['POST'])
@accept()
def register():
    name = request.json['name']
    username = request.json['username']
    password = request.json['password']

    if None in (name, username, password):
        raise ArgMissingError

    # Use string UUID to avoid conversion problems
    id = str(uuid4())

    new_Customer = Customer(id, name, username, password)
    db.session.add(new_Customer)
    db.session.commit()

    token = create_token(id)

    data = {'id': id, 'name': name, 'username': username, 'token':token}

    return customer_Schema.jsonify(data)

# Get new token
@app.route('/token', methods=['POST'])
@accept()
def get_token():
    username = request.json['username']
    password = request.json['password']

    if None in (username, password):
        raise ArgMissingError

    
    user = Customer.query.filter(Customer.username==username).first()

    if user.password != password:
        raise ApiAuthenticationError
        
    token = create_token(user.id)
    body = {'Token': token}

    return jsonify(body), 200
    


# Post analysis
@app.route('/analyze', methods=['POST'])
@accept()
def analyze():
    user = Customer.query.filter(username=username).first()
    if user.password != password:
        raise ApiAuthenticationError

    # Do the module stuff here and return


# Get analysis
@app.route('/analysis/<module_id>', methods=['GET'])
def get_analysis(module_id):
    try:
        module_id = int(module_id)
    except ValueError:
        raise ArgMissingError

    user = Customer.query.filter(username=username).first()
    if user.password != password:
        raise ApiAuthenticationError

    user_id = user.id

    analysis = Analysis.query.filter(customer_id=user_id, module_id=module_id).first()


# Get all analyses
