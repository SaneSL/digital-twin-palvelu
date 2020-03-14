from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import EncryptedType, PasswordType, force_auto_coercion
from app import db


force_auto_coercion()

secret_key = 'secretkey1234'


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512']))
    sub_end = db.Column(db.Date)
    results = db.relationship('Result', backref='customer')

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    
    def __init__(self, module_id, customer_id):
        self.module_id = module_id
        self.customer_id = customer_id


if __name__ == "__main__":
    # Run this file directly to create the database tables
    print ("Creating database tables...")
    db.drop_all()
    db.create_all()
    print ("Done!")