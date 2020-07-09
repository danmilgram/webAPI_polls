from flask import Response
import json

def raiseError():
    return Response(response=json.dumps({"Error": "Please provide connection information"}),status=400,mimetype='application/json')

def responseOK(res):
    return Response(response=json.dumps(res),status=200,mimetype='application/json')

def responseUP():
    return Response(response=json.dumps({"Status": "UP"}),status=200,mimetype='application/json')

def validationError(msg):
    return Response(response=json.dumps({"Validation error": msg}),status=400,mimetype='application/json')
