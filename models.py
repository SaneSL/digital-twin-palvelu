from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy_utils import EncryptedType, PasswordType, force_auto_coercion
from app import db, ma


force_auto_coercion()

secret_key = 'secretkey1234'


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(PasswordType(schemes=['pbkdf2_sha512', 'md5_crypt'], deprecated=['md5_crypt']))

    def __init__(self, name, username):
        self.name = name,
        self.username = username


# class Result(db.Model):



if __name__ == "__main__":

    # Run this file directly to create the database tables


    print "Creating database tables..."
    db.create_all()
    print "Done!