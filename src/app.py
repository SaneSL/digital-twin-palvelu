import os
import json
from flask import Flask, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from utils.models import db
from utils.schemas import ma
from utils.login_manager import loginManager
from views.home import home
from views.api import api


# Init app
app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(api, url_prefix='/api')


# Get config
with open('config.json') as json_data_file:
    cfg = json.load(json_data_file)

# Database
connString = "postgresql+psycopg2://{}:{}@{}/{}".format(cfg["pg_user"], cfg["pg_pw"], cfg["pg_host"], cfg["pg_db"])
app.config['SQLALCHEMY_DATABASE_URI'] = connString
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ghpahfgowfg'
 
# Init db
db.init_app(app)

# Init marsmallow
ma.init_app(app)

# Init login manager
loginManager.init_app(app)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
