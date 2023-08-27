import pytest
from fastapi.testclient import TestClient

from comprehensive_microservice.api_service import app, get_storage
from comprehensive_microservice.coder import Storage


@pytest.fixture()
def storage():
    return Storage()


@pytest.fixture()
def client(storage):
    app.dependency_overrides[get_storage] = lambda: storage

    return TestClient(app)


@pytest.fixture()
def correct_data():
    return {"text": "text", "title": "title"}


def test_correct_data(correct_data, client):
    response = client.post("/save", json=correct_data)
    assert "key" in response.json()
    assert response.json()["key"]


@pytest.mark.parametrize(
    "invalid_data",
    [
        {"title": 123},
        {"text": "text"},
        {"title": [1, 2, 3], "text": "GAV MYOW"},
    ],
)
def test_incorrect_input_json(invalid_data, client):
    response = client.post("/save", json=invalid_data)
    assert response.status_code != 200


def test_incorrect_key(client):
    response = client.get("/get/1000000")
    assert response.status_code == 404


def test_save_and_get(correct_data, client):
    response_post = client.post("/save", json=correct_data)
    key = response_post.json()["key"]
    response_get = client.get(f"/get/{key}")
    assert response_get.json() == correct_data
