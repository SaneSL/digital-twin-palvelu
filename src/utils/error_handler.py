from flask import Blueprint, jsonify
from utils.exceptions import *

error_handler = Blueprint('error_handler', __name__)


@error_handler.app_errorhandler(DatabaseError)
@error_handler.app_errorhandler(AuthenticationError)
@error_handler.app_errorhandler(InvalidArgError)
@error_handler.app_errorhandler(ModuleError)
@error_handler.app_errorhandler(ModuleArgError)
@error_handler.app_errorhandler(ModuleNotFound)
def handle_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response