import requests
import json
import jsonpath


def test_post_request():
    url = "https://reqres.in/api/users"

    file = open("/home/hp/PycharmProjects/pythonAPI/new 1.json", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    print(f"Json file is {request_json}")
    response = requests.post(url, request_json)
    print(f"Response file is {response.content}")
    assert response.status_code == 201
    print(f"Status code is {response.status_code}")
    print(response.headers)
    content = (response.headers.get("Content-Length"))
    print(f"Content is {content}")
    assert response.headers.get("Content-Length") == str(content)
    response_json = json.loads(response.text)
    print(response_json)
    id_json = jsonpath.jsonpath(response_json, "id")
    id = jsonpath.jsonpath(response_json, "id")
    print(f"Json id is {id_json[0]}")
    assert id_json == id

