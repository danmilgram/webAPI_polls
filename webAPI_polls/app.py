import flask
import pymongo
from routes import *
from utils import genericResponses
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def base():
    return genericResponses.responseUP()

app.register_blueprint(routes)

app.run()

