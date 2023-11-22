from typing import List

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from main import app
from src.database import SessionLocal

client = TestClient(app)


def test_get_connections_by_dmtt_id():
    with SessionLocal() as session:
        response = client.get("/connection/by_dmtt_id/1")
        assert response.status_code == 200


def test_get_connections_by_product_id():
    with SessionLocal() as session:
        response = client.get("/connection/by_product_id/1")
        assert response.status_code == 200


def test_create_list():
    product_data = [
        {"product_id": 1,
         "company_id": 1,
         "dmtt_id": 1},
        {"product_id": 1,
         "company_id": 1,
         "dmtt_id": 1},
        {"product_id": 1,
         "company_id": 1,
         "dmtt_id": 1}
    ]

    # Send a POST request to create a product
    response = client.post("/connection/create_list", json=product_data)
    assert response.status_code == 200
    created_product = response.json()
    # assert created_product["name"] == product_data["name"]


def test_get_connections_by_company_id():
    with SessionLocal() as session:
        response = client.get("/connection/by_company_id/1")
        assert response.status_code == 200
        assert isinstance(response.json(), List)
