from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    company_name = StringField('Company name', validators=[InputRequired()])
    email = StringField('Email', validators=[Email(), InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    sub = SelectField('Subscription', choices=[('1', '1 Month'), ('3', '3 Months'), ('6', '6 Months'), ('12', '12 Months')])
    submit = SubmitField('Register')