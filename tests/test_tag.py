import requests, json

#addTag --> validateFields & validateName

def test_tags_InvalidFields():
    data = {"tag":"soyuntag", "hola":"hola"}
    response = requests.request('POST','http://localhost:5000/tags/add',json=data)
    assert response.text == '{"Validation error": "Tag must contain only one field, named tag"}'
    assert response.status_code == 400

def test_tags_InvalidName():
    data = {"tag":"coronavirus"}
    response = requests.request('POST','http://localhost:5000/tags/add',json=data)
    assert response.text == '{"Validation error": "Tag name is already in use by another tag"}'
    assert response.status_code == 400
