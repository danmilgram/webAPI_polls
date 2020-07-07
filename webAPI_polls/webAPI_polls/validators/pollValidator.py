def ValidateData(data,validatortype):
    if data is None or data == {} or validatortype not in data:
        return False
    else:
        return True