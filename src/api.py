from flask import Flask, jsonify, request, Response, make_response
from app import app
from uuid import uuid4
from utils.checks import *
from utils.token import create_token
from schemas import *
from models import *
import jwt, datetime

# TODO:
# Min/max lenght for password and username
# Catch database errors


# Test
@app.route('/test', methods=['POST'])
@accept()
def testi():
    """ payload = {'yks': '111', 'kaks': '222'}
    raise DatabaseError('Test', payload=payload) """
    pass


# Register
@app.route('/register', methods=['POST'])
@accept()
def register():
    name = request.json['name']
    username = request.json['username']
    password = request.json['password']

    if None in (name, username, password):
        body = {"Error": "Missing arguments"}
        return jsonify(body), 403

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
        body = {"Error": "Missing arguments"}
        return jsonify(body), 403

    
    user = Customer.query.filter(Customer.username==username).first()

    if user.password != password:
        return
        # Authentication failed
        

    return jsonify({'y': 'd'}), 200
    


# Post analysis
@app.route('/analyze', methods=['POST'])
@accept()
def analyze():
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

    analysis = Analysis.query.filter(customer_id=user_id, module_id=module_id).first()


# Get all analyses
