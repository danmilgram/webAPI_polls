import pymongo
from flask_login import LoginManager,login_user, logout_user, login_required,current_user,user_logged_in
from flask import Flask, request, json, Response
from services import dbService
from utils import genericResponses
from validators import tagValidator, tagValidatorMessages
from . import routes

@routes.route('/tags', methods=['GET'])
@login_required
def tags_get():
    response = dbService.MongoAPI("tags").read()
    return genericResponses.responseOK(response)


@routes.route('/tags/add', methods=['POST'])
@login_required
def tags_post():
    data = request.json
    msg = tagValidator.ValidateTag(data)
    if msg == tagValidatorMessages.ok():
        tag = dbService.MongoAPI("tags").find_one("tag", data["tag"])
        msg = tagValidator.ValidateName(tag)
        if msg == tagValidatorMessages.ok():
            response = dbService.MongoAPI("tags").write(data)
            return genericResponses.responseOK(response)

    return genericResponses.validationError(msg)