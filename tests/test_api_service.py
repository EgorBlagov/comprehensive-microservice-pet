from fastapi.testclient import TestClient

from comprehensive_microservice.api_service import app

tester = TestClient(app)


def test_save():
    response = tester.post("/save")
    assert response.status_code == 200


def test_get():
    response = tester.get("/get")
    assert response.status_code == 200
