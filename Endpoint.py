from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_is_prime_endpoint():
    response = client.get("/IsPrime/4")
    assert response.status_code == 200
    assert response.json() == {"changed": False, "msg": "No es primo"}   

    response = client.get("/IsPrime/2")
    assert response.status_code == 200
    assert response.json() == {"changed": True, "msg": "Es primo"}   


def test_fibonacci_endpoint():
    response = client.get("fibonacci/1")
    assert response.status_code == 200
    assert response.json() == {"fibonacci": 1}

    response = client.get("fibonacci/8")
    assert response.status_code == 200
    assert response.json() == {"fibonacci": 21}



