from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_add():
    response = client.get("/add?a=10&b=20")

    assert response.status_code == 200
    assert response.json()["result"] == 30


def test_invalid_input():
    response = client.get("/add?a=hello&b=20")

    assert response.status_code == 422
