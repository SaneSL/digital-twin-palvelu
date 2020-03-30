from flask import Flask, jsonify, request, render_template, Blueprint, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user
from utils.forms import *
from utils.models import *


apidocs = Blueprint('apidocs', __name__, static_folder="static", template_folder="templates")
