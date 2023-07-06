from fastapi.testclient import TestClient
from fastapi import status
from src.app import app

client = TestClient(app=app)


def test_index_ok():
    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World!"}
