from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy_utils import EncryptedType
from app import db, ma


class Result(db.Model)