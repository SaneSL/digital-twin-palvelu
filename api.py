from flask import Flask, jsonify, request
from app import app
from schemas import *
from models import *


# Testing
@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Moro'})


# Register
@app.route('/register', methods=['POST'])
def register():
    name = request.args.get('name', default=None)
    username = request.args.get('username', default=None)
    password = request.args.get('password', default=None)

    new_Customer = Customer(name=name, username=username, password=password)

    db.session.add(new_Customer)
    db.session.commit()

    return CustomerSchema.jsonify(new_Customer)



# Post analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    username = request.args.get('username', default=None)
    password = request.args.get('password', default=None)

    user = Customer.query.filter(username=username).first()
    if user.password == password:
        return

    # Do the module stuff here and return





# Get analysis
@app.route('/analyze', methods=['GET'])
def get_analysis():
    username = request.args.get('username', default=None)
    password = request.args.get('password', default=None)

    user = Customer.query.filter(username=username).first()
    if user.password == password:
        return

    user_id = user.id

    results = Result.query.filter(customer_id=user_id).all()



