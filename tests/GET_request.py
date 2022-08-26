import requests
import json
import jsonpath


def test_get_request():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    js = json.loads(response.text)
    value = jsonpath.jsonpath(js, "total")
    assert value[0] == 12
    print(f"Status Code is {response.status_code}")
    print(f"Value Is {value}")

