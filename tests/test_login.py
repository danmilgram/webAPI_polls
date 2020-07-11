import requests, json
#SignUp --> signUpFields, userExists
#Login --> loginFields, userExist, Credentials
#Logout


def test_signUp_badsignUpFieds():
    data = {
    "nam":"Pepe Juan",
    "email": "pepito@hotmail.com",
    "password": "pep" }
    response = requests.request('POST','http://localhost:5000/signup',json=data)
    assert response.text == '{"Validation error": "User must contain name, email and password"}'
    assert response.status_code == 400

def test_signUp_userEmailExists():
    data = {
    "name":"Dan Milgram",
    "email": "ddmilgram@gmail.com",
    "password": "pep" }
    response = requests.request('POST','http://localhost:5000/signup',json=data)
    assert response.text == '{"Validation error": "Supplied email is already registered"}'
    assert response.status_code == 400


def test_login_ok():
    data = {
    "email": "ddmilgram@gmail.com",
    "password": "dancito" }
    response = requests.request('POST','http://localhost:5000/login',json=data)
    assert response.status_code == 200

def test_login_badLoginFields():
    data={
    "efmailss": "ddmilgram@gmail.com",
    "password": "dancito"}
    response = requests.request('POST','http://localhost:5000/login',json=data)
    assert response.text == '{"Validation error": "Login must contain username and password"}'
    assert response.status_code == 400

def test_login_notUser():
    data={
    "email": "nosoyusuario@gmail.com",
    "password": "prueba"}
    response = requests.request('POST','http://localhost:5000/login',json=data)
    assert response.text == '{"Validation error": "Supplied email is not registered"}'
    assert response.status_code == 400

def test_login_incorrectPWD():
    data={
    "email": "ddmilgram@gmail.com",
    "password": "prueba"}
    response = requests.request('POST','http://localhost:5000/login',json=data)
    assert response.text == '{"Validation error": "Users password is not correct"}'
    assert response.status_code == 400

def test_logout():
    response = requests.request('POST','http://localhost:5000/logout')
    assert response.status_code == 200



