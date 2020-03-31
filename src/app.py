import os
import json
from flask import Flask, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from utils.models import db
from utils.schemas import ma
from utils.login_manager import login_manager
from views.home import home
from views.api import api
from views.apidocs import apidocs


# Init app
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(home)
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(apidocs, url_prefix='/docs')

# Get config
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open('config.json') as json_data_file:
    cfg = json.load(json_data_file)

# Database
conn_string = "postgresql+psycopg2://{}:{}@{}/{}".format(cfg["pg_user"], cfg["pg_pw"], cfg["pg_host"], cfg["pg_db"])
app.config['SQLALCHEMY_DATABASE_URI'] = conn_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ghpahfgowfg'
 
# Add db
db.init_app(app)

# Add marsmallow
ma.init_app(app)

# Add login manager
login_manager.init_app(app)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
