#!api/bin/python3
""" Database file """

from flask import Flask
from init import db, ma
from product import Product

app = Flask(__name__)

# Setup database URL
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://abdul:Abdulrahman!1@localhost/api_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

# Init db and marshmallow
with app.app_context():
    db.create_all()
