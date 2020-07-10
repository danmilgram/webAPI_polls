import requests, json
#addAnswer --> ValidateFields,ValidatePoll,ValidateExpiration,ValidateQuestionsAndAnswers

def test_answer_invalidFields():
    data = {
    "pollid": "5f084523d60e8bd7f698f3a3",
    "name": "Futbol",
    "answers": {"¿De que equipo sos?": "Racing",
               "¿Jugas al futbol?": "Si",
               "Cuando jugas, de que posicion jugas?": "delantero"},
    "email": "ddmilgram@gmail.com",
    "soyunfield":"pepe"}
    response = requests.request('POST','http://localhost:5000/answers/add',json=data)
    assert response.text == '{"Validation error": "Answer must have pollid, user(email), name and answers"}'
    assert response.status_code == 400

def test_answer_invalidPoll():
    data = {
    "pollid": "5f084523d60e8bd7f69853a3",
    "name": "Futbol",
    "answers": {"¿De que equipo sos?": "Racing",
               "¿Jugas al futbol?": "Si",
               "Cuando jugas, de que posicion jugas?": "delantero"},
    "email": "ddmilgram@gmail.com"}
    response = requests.request('POST','http://localhost:5000/answers/add',json=data)
    assert response.text == '{"Validation error": "Poll does not exist"}'
    assert response.status_code == 400

def test_answer_expiredPoll():
    data = {
    "pollid": "5f086c6a460adecd594fd1af",
     "name": "Esta es OOTRA encuesta",
        "answers": "{'Pregunta 1': ['Respuesta 1', 'Respuesta 2', 'Respuesta 3', 'Respuesta 4']}",
        "email": "ddmilgram@gmail.com"}
    response = requests.request('POST','http://localhost:5000/answers/add',json=data)
    assert response.text == '{"Validation error": "Poll has already expired"}'
    assert response.status_code == 400

def test_answer_invalidQuestionsAnswers():
    data ={
        "pollid": "5f08e7085e1b7b126ff88234",
        "name": "Encuesta loca",
        "answers": "{'¿Te gustan las encuestas?': 'Si', '¿Cuantas encuestas haces por año?':sfsdfdfd}",
        "email": "ddmilgram@gmail.com"
    }
    response = requests.request('POST','http://localhost:5000/answers/add',json=data)
    assert response.text == '{"Validation error": "Answers didnt match with proposed. Please provide only one proposed answer for each proposed question"}'
    assert response.status_code == 400



