import json

class Poll():
    def __init__(self,name, expiration):
        self.name = name
        self.expiration = expiration
        self.questions = {}

#EJEMPLO DE POLL

poll = Poll("Esta es una encuesta", "22/7/2020")
questions = {}
answers = []

answers.append("Respuesta 1")
answers.append("Respuesta 2")
answers.append("Respuesta 3")
answers.append("Respuesta 4")

questions["Pregunta 1"] = answers

poll.questions=questions

print(poll.__dict__)













