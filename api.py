from flask import Flask, jsonify, request
from app import app
from schemas import *
from models import *

# Check for json type in all routes


# Testing
@app.route('/', methods=['GET'])
def get():
    if request.is_json is False:
        print('Not JSON type, return error)
    return jsonify({'msg': 'Moro'})


# Register
@app.route('/register', methods=['POST'])
def register():
    if request.is_json is False:
        print('Not JSON type, return error)
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
        print('Not JSON type, return error)

    username = request.json['username']
    password = request.json['password']

    user = Customer.query.filter(username=username).first()
    if user.password == password:
        return

    # Do the module stuff here and return





# Get analysis
@app.route('/analyze', methods=['GET'])
def get_analysis():
    if request.is_json is False:
        print('Not JSON type, return error)
    username = request.json['username']
    password = request.json['password']

    user = Customer.query.filter(username=username).first()
    if user.password == password:
        return

    user_id = user.id

    results = Result.query.filter(customer_id=user_id).all()



