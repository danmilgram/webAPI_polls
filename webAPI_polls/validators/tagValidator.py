from .tagValidatorMessages import *

def ValidateTag(data):
    if "tag" in data and len(data) == 1:
        return ok()
    else:
        return notValidTag()

def ValidateName(data):
    if data is None:
        return ok()
    else:
        return notValidTagName()
