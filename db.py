#!/usr/bin/python3

""" Database file """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

# Setup database URL
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://abdul:Abdulrahman!1@localhost/api_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Init db and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)
