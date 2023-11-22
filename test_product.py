from typing import List

from fastapi.testclient import TestClient

from main import app  # Assuming your FastAPI app instance is named "app"

client = TestClient(app)
token = ""
response = client.post(
    "/auth/login", json={"username": "admin", "password": "123"})
assert response.status_code == 200
tokens = response.json()
token = tokens["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# Test cases for Product endpoints


def test_create_product():
    # Define test data
    product_data = {
        "name": "Test Product",
        "measure": "Test Measure",
        "code": "TP123"
    }

    # Send a POST request to create a product
    response = client.post("/product/create", json=product_data)
    assert response.status_code == 200
    created_product = response.json()
    assert created_product["name"] == product_data["name"]


def test_read_products():
    # Send a GET request to retrieve all products
    response = client.get("/product/all")
    print(response.text)
    assert response.status_code == 200
    products = response.json()
    # Ensure that the response contains a list of products
    assert isinstance(products, list)
    # ... Add more assertions based on the expected behavior


def test_by_id():
    response = client.get("/product/1")
    assert response.status_code == 200
    product = response.json()
    # Ensure that the response contains a list of products
    assert product["id"] == 1


client = TestClient(app)


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
    stir_id = "87456325"  # Replace with an existing stir ID
    response = client.get(f"/company/{stir_id}", headers=headers)
    assert response.status_code == 404 or response.status_code == 200
    # Add assertions based on the expected response


def test_create_company():
    # Create a payload for company creation
    company_payload = {
        "name": "Company Name",
        "stir": "789456",
        "phone_number": "8465132"
    }
    response = client.post(
        "/company/create", json=company_payload, headers=headers)
    assert response.status_code == 200 or response.status_code == 422
    # Add assertions based on the expected response


def test_update_company():
    stir_id = 1  # Replace with an existing stir ID
    # Create a payload for company update
    company_update_payload = {
        "name": "Updated Company Name",
        "stir": "1267894",
        # "phone_number": "8465132"
    }
    response = client.put(
        f"/company/update/{stir_id}", json=company_update_payload, headers=headers)
    assert response.status_code == 200
    # Add assertions based on the expected response
