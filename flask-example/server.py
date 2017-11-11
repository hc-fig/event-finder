from flask import Flask
app = Flask(__name__)

from random import random

@app.route("/")
def hello():
    r = random()
    
    return "Hello World! Here's a random number: " + str(r)
