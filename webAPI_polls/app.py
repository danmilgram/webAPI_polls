import flask
import pymongo
from routes import *
from utils import genericResponses
from models import user
from flask_login import LoginManager
from services import dbService
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#FOR TESTING
#app.config["TESTING"] = True
#app.config["LOGIN_DISABLED"] = True

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    for us in user.users:
        if us.id == int(user_id):
            return us
    return None

@app.route('/')
def base():
    return genericResponses.responseUP()

app.register_blueprint(routes)
app.run()




