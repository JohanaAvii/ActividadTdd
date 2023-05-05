from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_is_prime_endpoint():
    response = client.get("/IsPrime/4")
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

    response = client.get("/IsPrime/2")
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}


def test_fibonacci_endpoint():
    response = client.get("fibonacci/1")
    assert response.status_code == 200
    assert response.json() == {"fibonacci": 1}

    response = client.get("fibonacci/8")
    assert response.status_code == 200
    assert response.json() == {"fibonacci": 21}



