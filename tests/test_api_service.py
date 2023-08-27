from fastapi.testclient import TestClient

from comprehensive_microservice.api_service import app

tester = TestClient(app)


def test_correct_data():
    data_json = {"text": "some text", "title": "some title"}
    response = tester.post("/save", json=data_json)
    assert "key" in response.json()
    assert response.json()["key"]


def test_incorrect_input_json():
    incorrect_jsons = [
        {"title": 123},
        {"text": "text"},
        {"title": [1, 2, 3], "text": "GAV MYOW"},
    ]

    for item in incorrect_jsons:
        response = tester.post("/save", json=item)
        assert response.status_code != 200


def test_incorrect_key():
    response = tester.get("/get/1000000")
    assert response.status_code == 404


def test_save_and_get():
    data = {"title": "slovo", "text": "tekst"}
    response_post = tester.post("/save", json=data)
    key = response_post.json()["key"]
    response_get = tester.get(f"/get/{key}")
    assert response_get.json() == data
