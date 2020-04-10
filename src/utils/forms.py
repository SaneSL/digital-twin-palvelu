from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    company_name = StringField('Company name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    sub = SelectField('Subscription', choices=[('1', '1 Month'), ('1', '3 Months'), ('1', '6 Months'), ('12', '12 Months')])
    submit = SubmitField('Register')