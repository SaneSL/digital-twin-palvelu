from flask import Flask, jsonify, request, render_template, Blueprint
from uuid import uuid4
from utils.checks import *
from utils.exceptions import *
from utils.forms import *
from utils.token import create_token
from schemas import customer_Schema, customers_Schema, analysis_Schema, analyses_Schema
from models import *


api = Blueprint('api', __name__, static_folder="static", template_folder="templates")

# TODO:
# Min/max lenght for password and username
# Catch database errors



@api.errorhandler(DatabaseError)
@api.errorhandler(ApiAuthenticationError)
@api.errorhandler(ArgMissingError)
def handle_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Register
@api.route('/register', methods=['POST'])
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
@api.route('/token', methods=['POST'])
@accept()
def get_token():
    username = request.json['username']
    password = request.json['password']

    if None in (username, password):
        raise ArgMissingError

    
    user = Customer.query.filter_by(username=username).first()

    if user.password != password:
        raise ApiAuthenticationError
        
    token = create_token(user.id)
    body = {'Token': token}

    return jsonify(body), 200
    


# Post analysis
@api.route('/analyze', methods=['POST'])
@accept()
def analyze():
    user = Customer.query.filter_by(username=username).first()
    if user.password != password:
        raise ApiAuthenticationError

    # Do the module stuff here and return


# Get analysis
@api.route('/analysis/<id>', methods=['GET'])
def get_analysis(id):
    try:
        id = int(id)
    except ValueError:
        raise ArgMissingError

    user = Customer.query.filter(username=username).first()
    if user.password != password:
        raise ApiAuthenticationError

    user_id = user.id

    analysis = Analysis.query.filter(customer_id=user_id, id=id).first()
    return analysis_Schema.jsonify(analysis)


# Get all analyses
@api.route('/analyses', methods=['GET'])
def get_analyses():
    user = Customer.query.filter(username=username).first()
    if user.password != password:
        raise ApiAuthenticationError

    user_id = user.id

    analysis = Analysis.query.filter(customer_id=user_id).all()
    return analyses_Schema.jsonify(analysis)