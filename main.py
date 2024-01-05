#!/home/abdul/Practicals/API/api/bin/python3

from db import app, db, ma
from flask import jsonify


people = [
    {
        "name": "Abdul",
        "age": 23,
        "address": "Kampala",
        "email": "abdulnsamba@gmail.com"
    },
    {
        "name": "Hassan",
        "age": 30,
        "address": "Jinja",
        "email": "hassan@gmail.com"
    }
]

@app.route('/api/products', strict_slashes=False, methods = ['GET'])
def products():
    """ Get products """
    return "API"

@app.route('/api/people', strict_slashes=False, methods = ['GET'])
def get_people():
    """ Gets all people in our database """
    return jsonify({'people': people})


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
