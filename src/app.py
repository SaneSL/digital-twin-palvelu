import os
import json
from flask import Flask, request, jsonify, url_for, g
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from utils.models import db
from utils.schemas import ma
from utils.login_manager import login_manager
from views.home import home
from views.api import api
from views.apidocs import apidocs
from modules.moduleapi import ModuleAPI
from utils.error_handler import error_handler
from flasgger import Swagger


template = {
  "swagger": "2.0",
  "info": {
    "version": "1.0.0",
    "title": "My API",
    "description": "description",
    "contact": {
      "name": "Sane",
      "url": "http://Sane.com",
      "email": "Sane@Sane.com"
    }
  }
}

def create_app(module_api):
    # Init app
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(home)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(apidocs, url_prefix='/docs')
    app.register_blueprint(error_handler)

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
    app.config['MODULE_API'] = module_api
    
    # Add db
    db.init_app(app)

    # Add marsmallow
    ma.init_app(app)

    # Add login manager
    login_manager.init_app(app)

    # Add swagger
    swagger = Swagger(app, template=template)

    return app

# Run Server
if __name__ == '__main__':
    module_api = ModuleAPI()
    app = create_app(module_api)
    app.run(debug=True)