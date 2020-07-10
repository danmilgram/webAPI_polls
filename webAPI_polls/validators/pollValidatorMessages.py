def notValidProp():
    return "Poll must contain (only) name, expiration, questions and tags"

def hasNoQuestion():
    return "Poll must contain at least one question"

def qtyAnswersExceded():
    return "Questions must have between 1 and 4 answers"

def notValidDateTime():
    return "Expiration date is not a valid datetime"

def notValidExpirationDate():
    return "Expiration date must be after todays date"

def Ok():
    return "Validation ok"

def Undefined():
    return "Please verify data formats"

def notValidName():
    return "Polls name is already in use by another poll"

