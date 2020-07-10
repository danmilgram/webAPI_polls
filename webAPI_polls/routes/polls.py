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
        poll = dbService.MongoAPI("polls").find_one("name",data["name"])
        msg = pollValidator.ValidateName(poll)
        if msg == pollValidatorMessages.Ok():

            pollresponse = dbService.MongoAPI("polls").write(data)

            for tag in data["tags"]:
                response = dbService.MongoAPI("tags").find_one("tag",tag)
                if response is None:
                    newtag = {"tag":tag}
                    response = dbService.MongoAPI("tags").write(newtag)

            return genericResponses.responseOK(pollresponse)

    return genericResponses.validationError(msg)





