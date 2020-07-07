import flask
import pymongo
from routes import *
from messages import genericResponses

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def base():
    return genericResponses.responseUP()

app.register_blueprint(routes)

app.run()

