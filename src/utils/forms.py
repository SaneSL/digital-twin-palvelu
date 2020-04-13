from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired, ValidationError
from utils.models import Customer

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

    def validate_email(self, email):
        user = Customer.query.filter_by(email=email.data).first()
        
        if user:
            raise ValidationError('Email already taken')

    def validate_username(self, username):
        user = Customer.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username already taken')