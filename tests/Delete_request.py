import requests


def test_delete_request():
    url = "https://reqres.in/api/users/2"
    response = requests.delete(url)
    print(f"Status code is {response.status_code}")
    assert response.status_code == 204
