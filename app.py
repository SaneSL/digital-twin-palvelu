from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://@localhost/"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
 
# Init db
db = SQLAlchemy(app)

# Init marsmallow
ma = Marshmallow(app)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
