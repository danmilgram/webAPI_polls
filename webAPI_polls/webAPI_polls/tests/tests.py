import requests
import json

class TestCase:
    def __init__(self,url,method,testName,data = None):
        self.url=url
        self.method=method
        self.testName=testName
        self.data=data

    def execute(self):
        response = requests.request(self.method,self.url, json = self.data)
        try:
            if (response.status_code != 200):
                assert False
            else:
                print(self.testName + " ejecutado correctamente")
        except AssertionError as e:
            print("AssertionError:", str(e) + str(response.text))

data = {}

test_getClients = TestCase("http://localhost:5000/clients", "GET", "test_getClients")
test_getClients.execute()

data["Document"] = {"nombre": "prueba", "apellido":"pruebita", "mail":"prueba@prueba.com.ar", "direccion":"dirprueba", "telefono":"1231231223", "origen":"unorigen"}
test_addClient = TestCase("http://localhost:5000/clients/add", "POST", "test_addClient", data)
test_addClient.execute()

data = {"Filter":{"nombre":"prueba"},
        "DataToBeUpdated":{"nombre": "prueba2", "apellido":"pruebita2", "mail":"prueba2@prueba.com.ar", "direccion":"dirprueba2", "telefono":"12312312232", "origen":"unorigen"}}
test_updateClient = TestCase("http://localhost:5000/clients/update", "PUT", "test_updateClient", data)
test_updateClient.execute()

data = {"Filter":{"nombre":"prueba"}}
test_deleteClient = TestCase("http://localhost:5000/clients/delete", "DELETE", "test_deleteClient", data)
test_deleteClient.execute()


