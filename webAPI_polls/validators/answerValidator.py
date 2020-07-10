from .answerValidatorMessages import *
import datetime

def ValidateAnswer(data):
    return ok()

def ValidateProperties(data):
    if "pollid" not in data or "answers" not in data or "email" and "name" not in data:
        return notValidProperties()
    else:
        return ok()

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