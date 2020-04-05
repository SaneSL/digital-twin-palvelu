from flask import Flask, jsonify, request, render_template, Blueprint, current_app
from uuid import uuid4
from utils.checks import *
from utils.exceptions import *
from utils.forms import *
from utils.token_jwt import create_token
from utils.schemas import customer_Schema, customers_Schema, analysis_Schema, analyses_Schema
from utils.models import *
from modules.moduleapi import ModuleAPI
import datetime


api = Blueprint('api', __name__, static_folder="static", template_folder="templates")

# TODO:
# Min/max lenght for password and username
# Catch database errors
# Maybe add token blacklist for users to add tokens to
# Dont return schema because if that fails stuff is already in DB


# Register
@api.route('/register', methods=['POST'])
@accept()
def register():
    name = request.json.get('name')
    username = request.json.get('username')
    password = request.json.get('password')

    if None in (name, username, password):
        raise InvalidArgError

    # Use string UUID to avoid conversion problems
    id = str(uuid4())

    # Default subscription time is 30 days
    sub_end = datetime.date.today() + datetime.timedelta(days=30)

    new_customer = Customer(id, name, username, password, sub_end)
    db.session.add(new_customer)
    db.session.commit()

    token = create_token(id)

    return customer_Schema.jsonify(new_customer)


# Get new token
@api.route('/token', methods=['POST'])
@accept()
def get_token():
    username = request.json.get('username')
    password = request.json.get('password')

    if None in (username, password):
        raise InvalidArgError

    user = Customer.query.filter_by(username=username).first()

    if user is None or user.password != password:
        raise ApiAuthenticationError
        
    token = create_token(user.id, user.sub_end)
    body = {'token': token}

    return jsonify(body)
    

# Post analysis
@api.route('/analyze', methods=['POST'])
@accept()
@token_required
def analyze(user_id):
    # Maybe check variables before allowing to pass them to module with class.__dict__.keys()
    
    data = request.json.get('data')
    module_id = request.json.get('module_id')

    # Useless because accept()?
    if None in (data, module_id) or not isinstance(data, dict):
        raise InvalidArgError

    module = current_app.config['MODULE_API'].factory.get_module(1, data)
    results = module.run()

    # Module returns invalid type
    if not isinstance(results, dict):
        raise ModuleError
    
    new_analysis = Analysis(results, user_id)
    db.session.add(new_analysis)
    db.session.commit()

    return analysis_Schema.jsonify(new_analysis)


# Get analysis
@api.route('/analysis', methods=['GET'])
@token_required
def get_analysis(user_id):
    id = request.json.get('id')

    # Maybe invalid argument better
    try:
        id = int(id)
    except:
        raise InvalidArgError

    analysis = Analysis.query.filter_by(id=id, customer_id=user_id).first()
    return analysis_Schema.jsonify(analysis)


# Get all analyses
@api.route('/analyses', methods=['GET'])
@token_required
def get_analyses(user_id):
    analyses = Analysis.query.filter_by(customer_id=user_id).all()

    if analyses is None:
        return jsonify({})

    return analyses_Schema.jsonify(analyses)


@api.route('/test')
@token_required
def testeri(user_id):
    print(user_id)
    return jsonify({'Done': 'Done'})