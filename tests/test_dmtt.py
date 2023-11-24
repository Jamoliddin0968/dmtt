import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from typing import List

from fastapi.testclient import TestClient

from main import app  



client = TestClient(app)
token = ""
response = client.post(
    "/auth/login", json={"username": "admin", "password": "123"})
assert response.status_code == 200
tokens = response.json()
token = tokens["access_token"]
headers = {"Authorization": f"Bearer {token}"}




def test_get_all_dmtt():
    response = client.get(
        "/dmtt/all", headers=headers)
    assert isinstance(response.json(),List )


def test_get_dmtt():
    id = 1  # Replace with an existing stir ID
    response = client.get(f"/dmtt/{id}", headers=headers)
    assert response.status_code == 404 or response.status_code == 200
    # Add assertions based on the expected response


def test_create_dmtt():
    company_payload = {
        "name": "Company Name",
        "person":"user1",
        "stir": "789456",
        "phone_number": "8465132"
    }
    response = client.post(
        "/dmtt/create", json=company_payload, headers=headers)
    assert response.status_code == 200 or response.status_code == 422
    if response.status_code == 422:
        assert response.json()["detail"]=="Bu STIR li foydalanuvchi allaqachon mavjud"


def test_update_dmtt():
    id = 1
    company_update_payload = {
        "name": "Updated Company Name",
        "phone_number": "1267894",
        "person":"user2",
        "stir":"dfvdf"
    }
    response = client.put(
        f"/company/update/{id}", json=company_update_payload, headers=headers)
    assert response.status_code == 200
    if response.status_code == 200:
        assert response.json()["phone_number"]== "1267894"
        
def test_delete_dmtt():
    id = -1
    response = client.delete(f'dmtt/delete/{id}',headers=headers)
    assert response.status_code == 404
    
    for i in range(1,10):
        if client.get(f"/dmtt/{i}", headers=headers).status_code == 200:
            response = client.delete(f'dmtt/delete/{i}',headers=headers)
            assert response.status_code == 200
