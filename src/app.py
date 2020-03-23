import os
import json
from flask import Flask, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Init app
app = Flask(__name__)

# Get config
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open('config.json') as json_data_file:
    cfg = json.load(json_data_file)

# Database
connString = "postgresql+psycopg2://{}:{}@{}/{}".format(cfg["pg_user"], cfg["pg_pw"], cfg["pg_host"], cfg["pg_db"])
app.config['SQLALCHEMY_DATABASE_URI'] = connString
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ghpahfgowfg'
 
# Init db
db = SQLAlchemy(app)

# Init marsmallow
ma = Marshmallow(app)

# Run Server
if __name__ == '__main__':
    from api import *

    app.run(debug=True)
