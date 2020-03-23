from flask import Flask, jsonify, request, render_template, Blueprint, flash, redirect, url_for
from utils.forms import *
from models import *

home = Blueprint('home', __name__, static_folder="static", template_folder="templates")

# Test
@home.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(password)

        user = Customer.query.filter_by(username=username).first()
        print(user.username)
        if user.password != password:
            return jsonify({"Error": "Error"}), 400
        else:
            return redirect(url_for('home.get_home'))

    return render_template('login.html', form=form)


# Test 2
@home.route('/home')
def get_home():
    return render_template('layout.html')