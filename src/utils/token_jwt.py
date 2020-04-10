from flask import current_app
import jwt
import datetime

# Tokens typically last one day
def create_token(id, sub_end=None):

    # Create token with less than 1 day left on sub
    if sub_end == datetime.date.today() and sub_end is not None:
        dt = datetime.datetime.utcnow()
        day_ends_in = ((24 - dt.hour - 1) * 60 * 60) + ((60 - dt.minute - 1) * 60) + (60 - dt.second)

        token = jwt.encode({'id': id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=day_ends_in)}, current_app.config['SECRET_KEY'])
        return token.decode('utf-8')

    else:
        token = jwt.encode({'id': id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=1)}, current_app.config['SECRET_KEY'])
        return token.decode('utf-8')