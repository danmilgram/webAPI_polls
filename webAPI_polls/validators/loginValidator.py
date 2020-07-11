from flask_login import LoginManager,login_user, logout_user, login_required,current_user
from models import user
from utils import cryptography
from services import dbService

from .loginValidatorMessages import *

def ValidateSignUpFields(data):
    try:
        if "email" in data and "password" in data and "name" in data and len(data) == 3:
            return ok()
        else:
            return notValidSignUpFields()
    except Exception as e:
        return notValidSignUpFields()

def ValidateLoginFields(data):
    try:
        if "email" in data and "password" in data:
            return ok()
        else:
            return notValidLoginFields()
    except Exception as e:
        return  notValidLoginFields()

def ValidateCredentials(userpass, dbpass):
    if userpass.encode() == cryptography.decrypt(dbpass):
        return ok()
    else:
        return notValidCredentials()

def UserExist(response):
    if response is None:
        return notExist()
    else:
        return Exist()




