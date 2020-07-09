import pymongo
from flask import Flask, request, json, Response
from services import dbService
from utils import genericResponses
from validators import pollValidator, pollValidatorMessages
from . import routes

@routes.route('/polls', methods=['GET'])
def mongo_read():
    response = dbService.MongoAPI("polls","polls").read()
    return genericResponses.responseOK(response)

@routes.route('/polls/add', methods=['POST'])
def mongo_write():
    data = request.json
    msg = pollValidator.ValidatePoll(data)
    if msg == pollValidatorMessages.Ok():
        response = dbService.MongoAPI("polls","polls",data).write(data)
        return genericResponses.responseOK(response)
    else:
        return genericResponses.validationError(msg)

@routes.route('/polls/update', methods=['PUT'])
def mongo_update():
    data = request.json
    if pollValidator.ValidateData(data,"Filter"):
        response = dbService.MongoAPI(data).update()
        return genericResponses.responseOK(response)
    else:
        return genericResponses.raiseError()

@routes.route('/polls/delete', methods=['DELETE'])
def mongo_delete():
    data = request.json
    if pollValidator.ValidateData(data,"Filter"):
        response = dbService.MongoAPI(data).delete(data)
        return genericResponses.responseOK(response)
    else:
        return genericResponses.raiseError()



