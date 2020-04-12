from flask import Flask, render_template, Blueprint, current_app, redirect
from utils.checks import *
from utils.exceptions import *

docs = Blueprint('docs', __name__, static_folder="static", template_folder="templates")



@docs.route('/get_moduledocs')
def moduledocs():
    return redirect('docs/modules/work_modules/index.html')


@docs.route('/get_apidocs')
def apidocs():
    return redirect('/apidocs/')