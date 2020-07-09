from flask_login import LoginManager,login_user, logout_user, login_required,current_user
from models import user
from services import dbService

from .loginValidatorMessages import *

def ValidateSignUp(data):
    if "email" in data and "password" in data and "name" in data:
        return ok()
    else:
        return notValidSignUp()

def ValidateLogin(data):
    if "email" and "password" in data:
        return ok()
    else:
        return notValidLogin()

def ValidateCredentials(pass1, pass2):
    if user.decryptPass(pass1) == data[pass2].encode():
        return ok()
    else:
        return notValidCredentials()

def ValidateMail(response):
    if response is None:
        return ok()
    else:
        return notValidEMail()




