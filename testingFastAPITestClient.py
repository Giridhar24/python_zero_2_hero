# Topic of the Day: Testing FastAPI (TestClient)
#
# Explanation: You built an API yesterday.
#
# Now, let's write an automated test to prove it works.
#
# FastAPI provides a TestClient (based on httpx) that simulates a web browser hitting your API.
#
# Code: Note: Run pip install httpx first.

from fastapi.testclient import TestClient
from buildingAcrudApiFastApi import app  # Import the 'app' we created yesterday

client = TestClient(app)


def test_read_main():
    # 1. Simulate a GET request to "/"
    response = client.get("/items")

    # 2. Check status code (200 OK)
    assert response.status_code == 200

    # 3. Check the JSON response
    # (Assuming our DB started with {1: "Laptop", 2: "Mouse"})
    assert response.json() == {"1": "Laptop", "2": "Mouse"}


def test_create_item():
    # 1. Simulate POST
    response = client.post("/items/3?name=Keyboard")

    # 2. Assertions
    assert response.status_code == 200
    assert response.json() == {"message": "Created", "item": "Keyboard"}