from flask import Flask, jsonify, request, render_template, Blueprint
from utils.forms import *


home = Blueprint('home', __name__, static_folder="static", template_folder="templates")

# Test
@home.route('/login', methods=['GET', 'POST'])
def testi():
    form = LoginForm()
    print(form.username.data)
    print(form.password.data)
    return render_template('login.html', form=form)


# Test 2
@home.route('/home')
def xd():
    return render_template('layout.html')
