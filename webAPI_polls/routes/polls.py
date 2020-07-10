import pymongo
from flask_login import LoginManager,login_user, logout_user, login_required,current_user,user_logged_in
from flask import Flask, request, json, Response
from services import dbService
from utils import genericResponses
from validators import pollValidator, pollValidatorMessages
from . import routes

@routes.route('/polls', methods=['GET'])
@login_required
def polls_get():
    response = dbService.MongoAPI("polls").read()
    return genericResponses.responseOK(response)


@routes.route('/polls/add', methods=['POST'])
@login_required
def polls_post():
    data = request.json
    msg = pollValidator.ValidatePoll(data)
    if msg == pollValidatorMessages.Ok():
        response = dbService.MongoAPI("polls").write(data)
        return genericResponses.responseOK(response)
    else:
        return genericResponses.validationError(msg)

@routes.route('/polls/update', methods=['PUT'])
@login_required
def polls_put():
    data = request.json
    if pollValidator.ValidateData(data,"Filter"):
        response = dbService.MongoAPI(data).update()
        return genericResponses.responseOK(response)
    else:
        return genericResponses.raiseError()

@routes.route('/polls/delete', methods=['DELETE'])
@login_required
def polls_delete():
    data = request.json
    if pollValidator.ValidateData(data,"Filter"):
        response = dbService.MongoAPI(data).delete(data)
        return genericResponses.responseOK(response)
    else:
        return genericResponses.raiseError()




