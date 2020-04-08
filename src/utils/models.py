from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import UUIDType, PasswordType, JSONType, force_auto_coercion
from flask_login import UserMixin


db = SQLAlchemy()

force_auto_coercion()


class Customer(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512']))
    results = db.relationship('Analysis', backref='customer')

    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = password


class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    results = db.Column(JSONType)
    customer_id = db.Column(db.Text, db.ForeignKey(Customer.id), nullable=False)

    def __init__(self, results, customer_id):
        self.results = results
        self.customer_id = customer_id


class Sub(db.Model):
    customer_id = db.Column(db.String, db.ForeignKey(Customer.id), primary_key=True)
    end = db.Column(db.Date)
    period = db.Column(db.SmallInteger)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, customer_id, end, period):
        self.customer_id = customer_id
        self.end = end
        self.period = period

if __name__ == "__main__":
    from app import create_app
    import sys

    sys.path.append('..')
    app = create_app()

    with app.app_context():
        # Run this file directly to create the database tables
        print ("Creating database tables...")
        db.drop_all()
        db.create_all()
        print ("Done!")