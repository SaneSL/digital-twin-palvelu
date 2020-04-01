from flask import Flask, jsonify, request, render_template, Blueprint
from uuid import uuid4
from utils.checks import *
from utils.exceptions import *
from utils.forms import *
from utils.token_jwt import create_token
from utils.schemas import customer_Schema, customers_Schema, analysis_Schema, analyses_Schema
from utils.models import *
import datetime


api = Blueprint('api', __name__, static_folder="static", template_folder="templates")

# TODO:
# Min/max lenght for password and username
# Catch database errors
# Maybe add token blacklist for users to add tokens to
# Test new token stuff


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
    name = request.json.get('name', None)
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if None in (name, username, password):
        raise ArgMissingError

    # Use string UUID to avoid conversion problems
    id = str(uuid4())

    # Default subscription time is 30 days
    sub_end = datetime.date.today() + datetime.timedelta(days=30)

    new_Customer = Customer(id, name, username, password, sub_end)
    db.session.add(new_Customer)
    db.session.commit()

    token = create_token(id)

    data = {'id': id, 'name': name, 'username': username, 'token':token}

    return customer_Schema.jsonify(data)


# Get new token
@api.route('/token', methods=['POST'])
@accept()
def get_token():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if None in (username, password):
        raise ArgMissingError

    
    user = Customer.query.filter_by(username=username).first()

    if user.password != password:
        raise ApiAuthenticationError
        
    token = create_token(user.id, user.sub_end)
    body = {'token': token}

    return jsonify(body)
    

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
@token_required
def get_analysis(user_id, id):
    try:
        id = int(id)
    except ValueError:
        raise ArgMissingError

    analysis = Analysis.query.filter_by(id=id, customer_id=user_id).first()
    return analysis_Schema.jsonify(analysis)


# Get all analyses
@api.route('/analyses', methods=['GET'])
@token_required
def get_analyses(user_id):
    analysis = Analysis.query.filter_by(customer_id=user_id).all()
    return analyses_Schema.jsonify(analysis)


@api.route('/test')
@token_required
def testeri(user_id):
    print(user_id)
    return jsonify({'Done': 'Done'})