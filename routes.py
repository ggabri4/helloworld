import os
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@main.route("/about")
def about():
    return "This is a simple example of a Flask application."

@main.route("/greet/<string:name>")
def greet(name):
    return "Hello, {}!".format(name)