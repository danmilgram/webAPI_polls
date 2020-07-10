import datetime
from .pollValidatorMessages import *

def ValidateName(poll):
    if poll is None:
        return Ok()
    else:
        return notValidName()

def ValidateProperties(data):
    if "name" in data and "expiration" in data and "questions" in data and "tags" in data and len(data) == 4:
        return Ok()
    else:
        return notValidProp()

def ValidateDatetime(date_string):
    try:
        datetime.datetime.strptime(date_string,  "%d/%m/%Y")
    except ValueError:
        return notValidDateTime()

    return Ok()

def ValidateExpiration(date):
    date = datetime.datetime.strptime(date,  "%d/%m/%Y")
    if date <= datetime.datetime.today():
        return notValidExpirationDate()
    else:
        return Ok()

def ValidateQuestions(questions):
    if len(questions) > 0:
        for question,answers in questions.items():
            if not(len(answers) <= 4 and len(answers) > 0):
                return qtyAnswersExceded()
        return Ok()
    else:
        return hasNoQuestion()

def ValidatePoll(data):
    try:
        msg = ValidateProperties(data)
        if msg == Ok():
            msg = ValidateDatetime(data["expiration"])
            if msg == Ok():
                msg = ValidateExpiration(data["expiration"])
                if msg == Ok():
                    msg = ValidateQuestions(data["questions"])
        return msg
    except Exception as e:
        return Undefined()