from flask import Flask, jsonify, request, render_template, Blueprint, current_app
from uuid import uuid4
from utils.checks import *
from utils.exceptions import *
from utils.forms import *
from utils.token_jwt import create_token
from utils.schemas import customer_Schema, customers_Schema, analysis_Schema, analyses_Schema
from utils.models import *
from flasgger.utils import swag_from
import datetime
import os


api = Blueprint('api', __name__, static_folder="static", template_folder="templates")

# TODO:
# Min/max lenght for password and username
# Catch database errors
# Maybe add token blacklist for users to add tokens to
# Dont return schema because if that fails stuff is already in DB


# Get new token
@api.route('/token', methods=['GET'])
@accept()
@swag_from(os.path.join(os.getcwd(), 'docs', 'api_yaml', 'token.yml'))
def get_token():
    username = request.json.get('username')
    password = request.json.get('password')

    if None in (username, password):
        raise InvalidArgError

    user = Customer.query.filter_by(username=username).first()

    if user is None or user.password != password:
        raise AuthenticationError
    
    sub = Sub.query.filter_by(customer_id = user.id).first()

    if sub is None:
        raise DatabaseError

    token = create_token(user.id, sub.end)
    body = {'token': token}

    return jsonify(body)
    

# Post analysis
@api.route('/analyze', methods=['POST'])
@accept()
@token_required
@swag_from(os.path.join(os.getcwd(), 'docs', 'api_yaml', 'analyze.yml'))
def analyze(user_id):
    # Maybe check variables before allowing to pass them to module with class.__dict__.keys()
    
    data = request.json.get('data')
    module_id = request.json.get('module_id')

    # Useless because accept()?
    if None in (data, module_id) or not isinstance(data, dict):
        raise InvalidArgError

    module = current_app.config['MODULE_API'].factory.get_module(module_id, **data)

    results = module._run()

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
@swag_from(os.path.join(os.getcwd(), 'docs', 'api_yaml', 'analysis.yml'))
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
@swag_from(os.path.join(os.getcwd(), 'docs', 'api_yaml', 'analyses.yml'))
def get_analyses(user_id):
    analyses = Analysis.query.filter_by(customer_id=user_id).all()

    if analyses is None:
        return jsonify({})

    return analyses_Schema.jsonify(analyses)
