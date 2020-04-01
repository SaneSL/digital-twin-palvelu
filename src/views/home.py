from flask import Flask, jsonify, request, render_template, Blueprint, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user
from utils.forms import *
from utils.models import *


home = Blueprint('home', __name__, static_folder="static", template_folder="templates")


@home.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = Customer.query.filter_by(username=username).first()
        if user is None:
            return jsonify({"Error": "Error"}), 400

        if user.password != password:
            return jsonify({"Error": "Error"}), 400
        else:
            login_user(user, remember=True)
            flash('Logged in!', 'success')
            return redirect(url_for('home.get_home'))

    return render_template('login.html', form=form)


@home.route('/')
@home.route('/home')
def get_home():
    return render_template('layout.html')

@home.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.get_home'))