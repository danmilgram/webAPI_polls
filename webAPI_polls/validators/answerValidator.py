from .answerValidatorMessages import *

def ValidateAnswer(data):
    return ok()

def ValidateProperties(data):
    if "pollid" not in data or "answers" not in data or "email" not in data:
        return notValidProperties()
    else:
        return ok()

def ValidatePoll(data):
    if data is None:
        return notValidPoll()
    else:
        return ok()

def ValidateQuestionsAndAnswers(pollQuestions, answeredQuestions):
    shared_items = {k: pollQuestions[k] for k in pollQuestions if k in answeredQuestions and answeredQuestions[k] in pollQuestions[k]}
    if len(shared_items) == len(pollQuestions) ==len(answeredQuestions):
        return ok()
    else:
        return notValidAnswers()