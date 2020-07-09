from flask_login import LoginManager,login_user, logout_user, login_required,current_user,user_logged_in
from validators import loginValidator,loginValidatorMessages
from flask import Flask, request, json, Response
from models import user
from utils import genericResponses
from services import dbService
from . import routes

def Login(data):
    email = data["email"]
    name = data["name"]
    password = data["password"]
    us = user.User(len(user.users) + 1, name, email, password)
    login_user(us)

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return genericResponses.responseOK(loginValidatorMessages.ok())
    else:
        data = request.json
        msg = loginValidator.ValidateLogin(data)
        if msg == loginValidatorMessages.ok():
            response = dbService.MongoAPI("polls","users").find_one("email",data["email"])
            msg = loginValidator.validateCredentials(data["password"], response["password"])
            if msg == loginValidatorMessages.ok():
                Login(data)
                return genericResponses.responseOK(msg)
            else:
                return genericResponses.validationError(msg)
        else:
            return genericResponses.validationError(msg)

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return genericResponses.responseOK("Loged out succesfully")

@routes.route("/signup", methods=["GET", "POST"])
def signUp():
    data = request.json
    msg = loginValidator.ValidateSignUp(data)
    if msg == loginValidatorMessages.signUpOk():
        data = request.json
        response = dbService.MongoAPI("polls","users").find_one("email",data["email"])
        msg = loginValidator.ValidateMail(response)
        if msg == loginValidatorMessages.ok():
            data["password"] = user.encryptPass(data["password"].encode())
            response = dbService.MongoAPI("polls","users",data).write(data)
            Login(data)
            return genericResponses.responseOK(response)
        else:
            return genericResponses.validationError(msg)
    else:
        return genericResponses.validationError(msg)


