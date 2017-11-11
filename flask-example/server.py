
# Import the flask module
from flask import Flask

# make a new flask app
app = Flask(__name__)

# for random numbers in one of the examples
from random import random


# @app.route is used to determine how pages are given to the users.
# When a user requests `localhost:5000/`, they are given the result
# of whatever function is tagged with @app.route("/")
@app.route("/")
def hello():
    r = random()

    # The user gets whatever the function returns.
    # This can be any string. It can be an entire file,
    # although there may be a better way to server files with flask.
    return "Hello World! Here's a random number: " + str(r)


# This function is tagged with @app.route("/example/"), so
# it is given when the user asks for `localhost:5000/example/`.
@app.route("/example/")
def another_route():
    return "This is another route that someone could go to"
