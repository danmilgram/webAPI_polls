from flask_login import LoginManager,login_user, logout_user, login_required,current_user,user_logged_in
from validators import loginValidator,loginValidatorMessages
from flask import Flask, request, json, Response
from models import user
from utils import cryptography
from utils import genericResponses
from services import dbService
from . import routes

def Login(data):
    email = data["email"]
    password = data["password"]
    us = user.User(len(user.users) + 1, email, password)
    login_user(us)

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return genericResponses.responseOK(loginValidatorMessages.ok())
    else:
        data = request.json
        msg = loginValidator.ValidateLoginFields(data)
        if msg == loginValidatorMessages.ok():
            response = dbService.MongoAPI("users").find_one("email",data["email"])
            msg = loginValidator.UserExist(response)
            if msg == loginValidatorMessages.Exist():
                msg = loginValidator.ValidateCredentials(data["password"], response["password"])
                if msg == loginValidatorMessages.ok():
                    Login(data)
                    return genericResponses.responseOK(msg)

        return genericResponses.validationError(msg)

@routes.route('/logout', methods=["POST"])
@login_required
def logout():
    logout_user()
    return genericResponses.responseOK("Loged out succesfully")

@routes.route("/signup", methods=["GET", "POST"])
def signUp():
    data = request.json
    msg = loginValidator.ValidateSignUpFields(data)
    if msg == loginValidatorMessages.ok():
        data = request.json
        response = dbService.MongoAPI("users").find_one("email",data["email"])
        msg = loginValidator.UserExist(response)
        if msg == loginValidatorMessages.notExist():
            data["password"] = cryptography.encrypt(data["password"].encode())
            response = dbService.MongoAPI("users").write(data)
            Login(data)
            return genericResponses.responseOK(response)

    return genericResponses.validationError(msg)


