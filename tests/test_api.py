import pytest
import requests
import requests_mock


class TestAPI:

    def test_api_get_request(self, setup_function):
        with requests_mock.Mocker() as mock:
            mock.get("http://example.com/api/users", json={"users": ["Alice", "Bob"]})
            response = requests.get("http://example.com/api/users")
            assert response.status_code == 200
            assert "users" in response.json()

    def test_api_post_request(self, setup_function):
        with requests_mock.Mocker() as mock:
            mock.post("http://example.com/api/users", json={"status": "success"}, status_code=201)
            response = requests.post("http://example.com/api/users", json={"name": "Alice"})
            assert response.status_code == 201
            assert response.json()["status"] == "success"
    ## this
    #lalala