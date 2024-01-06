#!/usr/bin/python3
""" Product module"""

from init import db, ma


# define user model
class Product(db.Model):
    """ Product database model"""
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# define user schema
class ProductSchema(ma.Schema):
    """ Marsh schema """
    class Meta:
        fields = ("name", "desc", "price")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
