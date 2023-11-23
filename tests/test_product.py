import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app  # Assuming your FastAPI app instance is named "app"
from fastapi.testclient import TestClient
from typing import List



# Append the parent directory of the current file (tests directory) to the Python path


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
        "code": "TP123",
        "winter":True
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
    response = client.get("/detail/product/1")
    if response.status_code == 200:
        assert response.status_code == 200
        product = response.json()
        assert product["id"] == 1
    else:
        response.status_code == 404
    # Ensure that the response contains a list of products
    



def test_read_winter_products():
    response = client.get("/product/winter")
    assert response.status_code == 200
    assert isinstance(response.json(),List)

# Similarly, write tests for other seasonal endpoints
def test_read_summer_products():
    response = client.get("/product/summer")
    assert response.status_code == 200
    # Assert other conditions based on the expected data
    
def test_read_spring_products():
    response = client.get("/product/spring")
    assert response.status_code == 200
    # Assert other conditions based on the expected data

def test_read_autumn_products():
    response = client.get("/product/autumn")
    assert response.status_code == 200
    # Assert other conditions based on the expected data