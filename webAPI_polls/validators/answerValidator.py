from .answerValidatorMessages import *
import datetime

def ValidateProperties(data):
    if "pollid" in data and "answers" in data and "email" in data and "name" in data and len(data)==4:
        return ok()
    else:
        return notValidProperties()

def ValidatePoll(data):
    if data is None:
        return notValidPoll()
    else:
        return ok()

def ValidateExpiration(date):
    date = datetime.datetime.strptime(date,  "%d/%m/%Y")
    if date <= datetime.datetime.today():
        return expiredPoll()
    else:
        return ok()

def ValidateQuestionsAndAnswers(pollQuestions, answeredQuestions):
    shared_items = {k: pollQuestions[k] for k in pollQuestions if k in answeredQuestions and answeredQuestions[k] in pollQuestions[k]}
    if len(shared_items) == len(pollQuestions) ==len(answeredQuestions):
        return ok()
    else:
        return notValidAnswers()