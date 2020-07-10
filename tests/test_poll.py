import requests,json

#Add Poll -->ValidateName, ValidateFields, ValidateDateTime, ValidateExpiration, ValidateQuestions

def test_invalidName():
    data = {
    "name": "Prueba",
    "expiration": "10/12/2020",
    "questions": {"¿Te gustan las pruebas?": ["Si", "No"]},
    "tags":["corona", "etiqueta nueva"]
    }
    response = requests.request('POST','http://localhost:5000/polls/add',json = data)
    assert response.text == '{"Validation error": "Polls name is already in use by another poll"}'
    assert response.status_code == 400

def test_invalidPollFields():
    data = {
    "names": "Prueba",
    "expirgation": "10/12/2020",
    "questions": {"¿Te gustan las pruebas?": ["Si", "No"]},
    "tags":["corona", "etiqueta nueva"]
    }
    response = requests.request('POST','http://localhost:5000/polls/add',json = data)
    assert response.text == '{"Validation error": "Poll must contain (only) name, expiration, questions and tags"}'
    assert response.status_code == 400

def test_invalidDateTime():
    data = {
    "name": "UnaPoll",
    "expiration": "fdf",
    "questions": {"¿Te gustan las pruebas?": ["Si", "No"]},
    "tags":["corona", "etiqueta nueva"]
    }
    response = requests.request('POST','http://localhost:5000/polls/add',json = data)
    assert response.text == '{"Validation error": "Expiration date is not a valid datetime"}'
    assert response.status_code == 400

def test_invalidExpirationDate():
    data = {
    "name": "UnaPoll",
    "expiration": "01/01/2010",
    "questions": {"¿Te gustan las pruebas?": ["Si", "No"]},
    "tags":["corona", "etiqueta nueva"]
    }
    response = requests.request('POST','http://localhost:5000/polls/add',json = data)
    assert response.text == '{"Validation error": "Expiration date must be after todays date"}'
    assert response.status_code == 400

def test_invalidQuestions():
    data = {
    "name": "UnaPoll",
    "expiration": "01/01/2021",
    "questions": {"¿Te gustan las pruebas?":[]},
    "tags":["corona", "etiqueta nueva"]
    }
    response = requests.request('POST','http://localhost:5000/polls/add',json = data)
    assert response.text == '{"Validation error": "Questions must have between 1 and 4 answers"}'
    assert response.status_code == 400