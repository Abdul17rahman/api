#!/usr/bin/python3
""" Product module"""

from db import db, ma


# define user model
class Product(db.model):
    """ Product database model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# define user schema
class ProductSchema(ma.Schema):
    """ Marsh schema """
    class Meta:
        feilds = ("name", "desc", "price")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
