from flask import Flask, render_template, Blueprint, current_app, redirect
from utils.checks import *
from utils.exceptions import *

docs = Blueprint('docs', __name__, static_folder="static", template_folder="templates")



@docs.route('/moduledocs')
def module_docs():
    return redirect('docs/modules/work_modules/index.html')