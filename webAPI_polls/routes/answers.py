import pymongo
from flask import Flask, request, json, Response
from services import dbService
from utils import genericResponses
from validators import answerValidator, answerValidatorMessages
from . import routes

@routes.route('/answers/getbyuser', methods=['GET'])
def answers_getbyuser():
    data = request.json
    response = dbService.MongoAPI("answers").find("email",data["email"])
    print(response)
    return genericResponses.responseOK(response)

@routes.route('/answers', methods=['GET'])
def answers_get():
    response = dbService.MongoAPI("answers").read()
    return genericResponses.responseOK(response)

@routes.route('/answers/add', methods=['POST'])
def answers_post():
    data = request.json
    msg = answerValidator.ValidateProperties(data)

    if msg == answerValidatorMessages.ok():
        poll = dbService.MongoAPI("polls").find_byid(data["pollid"])
        msg = answerValidator.ValidatePoll(poll)

        if msg == answerValidatorMessages.ok():
            msg = answerValidator.ValidateQuestionsAndAnswers(poll["questions"],data["answers"])

            if msg == answerValidatorMessages.ok():
                response = dbService.MongoAPI("answers").write(data)
                return genericResponses.responseOK(response)

    return genericResponses.validationError(msg)

