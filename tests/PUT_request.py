import requests
import json


def test_post_request():
    url = "https://reqres.in/api/users/2"

    file = open("/home/hp/PycharmProjects/pythonAPI/new 2.json", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    print(f"Json file is {request_json}")
    response = requests.put(url, request_json)
    print(f"Response file is {response.content}")
    assert response.status_code == 200
    print(response.status_code)
