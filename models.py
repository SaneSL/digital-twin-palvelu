from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy_utils import EncryptedType, PasswordType, force_auto_coercion
from app import db, ma


force_auto_coercion()

secret_key = 'secretkey1234'


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String(16), nullable=False)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512', 'md5_crypt'], deprecated=['md5_crypt']))
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
    db.create_all()
    print ("Done!")