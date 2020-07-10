def ok():
    return "ok"

def notValidProperties():
    return "Answer must have pollid, user(email), name and answers"

def notValidPoll():
    return "Poll does not exist"

def expiredPoll():
    return "Poll has already expired"

def notValidUser():
    return "User does not exist"

def notValidAnswers():
    return "Answers didnt match with proposed. Please provide only one proposed answer for each proposed question"