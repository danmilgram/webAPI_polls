from flask_login import LoginManager,login_user, logout_user, login_required,current_user
from models import user
from services import dbService

from .loginValidatorMessages import *

def ValidateSignUpFields(data):
    if "email" in data and "password" in data and "name" in data:
        return ok()
    else:
        return notValidSignUpFields()

def ValidateLoginFields(data):
    if "email" and "password" in data:
        return ok()
    else:
        return notValidLoginFields()

def ValidateCredentials(userpass, dbpass):
    if userpass.encode() == user.decryptPass(dbpass):
        return ok()
    else:
        return notValidCredentials()

def UserExist(response):
    if response is None:
        return notExist()
    else:
        return Exist()




