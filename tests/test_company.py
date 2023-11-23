import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from typing import List

from fastapi.testclient import TestClient

from main import app  # Assuming your FastAPI app instance is named "app"

# Append the parent directory of the current file (tests directory) to the Python path



client = TestClient(app)
token = ""
response = client.post(
    "/auth/login", json={"username": "admin", "password": "123"})
assert response.status_code == 200
tokens = response.json()
token = tokens["access_token"]
headers = {"Authorization": f"Bearer {token}"}


def test_search_company():
    response = client.get("/company/search/your_search_term")
    assert response.status_code == 200
    # Add assertions based on the expected response


def test_get_all_company():
    response = client.get(
        "/company/all", headers=headers)
    assert response.status_code == 200
    # Add assertions based on the expected response


def test_get_company():
    id = "1"  # Replace with an existing stir ID
    response = client.get(f"/company/{id}", headers=headers)
    assert response.status_code == 404 or response.status_code == 200
    # Add assertions based on the expected response


def test_create_company():
    company_payload = {
        "name": "Company Name",
        "stir": "789456",
        "phone_number": "8465132"
    }
    response = client.post(
        "/company/create", json=company_payload, headers=headers)
    assert response.status_code == 200 or response.status_code == 422


def test_update_company():
    id = 1
    company_update_payload = {
        "name": "Updated Company Name",
        "phone_number": "1267894"
    }
    response = client.put(
        f"/company/update/{id}", json=company_update_payload, headers=headers)
    assert response.status_code == 200
