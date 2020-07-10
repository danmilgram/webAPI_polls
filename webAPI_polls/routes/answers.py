import pymongo
from flask import Flask, request, json, Response
from flask_login import LoginManager,login_user, logout_user, login_required,current_user,user_logged_in
from services import dbService
from utils import genericResponses
from validators import answerValidator, answerValidatorMessages
from . import routes

@routes.route('/answers/getbyuser', methods=['GET'])
@login_required
def answers_getbyuser():
    data = request.json
    response = dbService.MongoAPI("answers").find("email",data["email"])
    return genericResponses.responseOK(response)

@routes.route('/answers', methods=['GET'])
@login_required
def answers_get():
    response = dbService.MongoAPI("answers").read()
    return genericResponses.responseOK(response)

@routes.route('/answers/add', methods=['POST'])
def answers_post():
    data = request.json
    msg = answerValidator.ValidateProperties(data)

    if msg == answerValidatorMessages.ok():
        poll = dbService.MongoAPI("polls").find_one("_id",data["pollid"])
        msg = answerValidator.ValidatePoll(poll)

        if msg == answerValidatorMessages.ok():
            msg = answerValidator.ValidateExpiration(poll["expiration"])

            if msg == answerValidatorMessages.ok():
                msg = answerValidator.ValidateQuestionsAndAnswers(poll["questions"],data["answers"])

                if msg == answerValidatorMessages.ok():
                    response = dbService.MongoAPI("answers").write(data)
                    return genericResponses.responseOK(response)

    return genericResponses.validationError(msg)

