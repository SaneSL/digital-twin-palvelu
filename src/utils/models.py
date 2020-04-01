from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import UUIDType, PasswordType, JSONType, force_auto_coercion
from flask_login import UserMixin
from utils.login_manager import login_manager


db = SQLAlchemy()

force_auto_coercion()


class Customer(db.Model, UserMixin):
    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512']))
    sub_end = db.Column(db.Date)
    results = db.relationship('Analysis', backref='customer')

    def __init__(self, id, name, username, password, sub_end):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.sub_end = sub_end


class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    results = db.Column(JSONType)
    customer_id = db.Column(db.Text, db.ForeignKey('customer.id'), nullable=False)


    def __init__(self, results, customer_id):
        self.results = results
        self.customer_id = customer_id


if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from app import app

    # Run this file directly to create the database tables
    with app.app_context():
        print ("Creating database tables...")
        db.drop_all()
        db.create_all()
        print ("Done!")