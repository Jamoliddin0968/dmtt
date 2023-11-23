import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.database import SessionLocal
from main import app
from fastapi.testclient import TestClient
from typing import List



# Append the parent directory of the current file (tests directory) to the Python path


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
    response = client.post("/connection/create_list", json=product_data)
    assert response.status_code == 200 or response.status_code == 404
    created_product = response.json()


def test_get_connections_by_company_id():
    with SessionLocal() as session:
        response = client.get("/connection/by_company_id/1")
        assert response.status_code == 200
        assert isinstance(response.json(), List)
