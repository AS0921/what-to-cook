from fastapi.testclient import TestClient

from app_final import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.json()


def test_get_recipe():
    response = client.get("/recipes/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Омлет"


def test_recipe_not_found():
    response = client.get("/recipes/999")
    assert response.status_code == 404


def test_match_finds_recipe():
    response = client.get("/match", params={"products": "яйца, молоко, соль"})
    assert response.status_code == 200
    data = response.json()
    assert data["found"] > 0
    first = data["recipes"][0]
    assert first["name"] == "Омлет"
    assert first["missing"] == []


def test_match_empty_products():
    response = client.get("/match", params={"products": ",,,"})
    assert response.status_code == 400