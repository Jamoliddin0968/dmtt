from typing import List

from fastapi.testclient import TestClient

from main import app  # Assuming your FastAPI app instance is named "app"

client = TestClient(app)

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


def test_company():
    response = client.get("/company/all")
    assert response.status_code == 200
    content = response.json()
    # Ensure that the response contains a list of products
    assert isinstance(content, List)
