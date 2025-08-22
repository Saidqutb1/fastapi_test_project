import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_create_task():
    response = client.post("/tasks/", json={"title": "Test", "description": "Desc"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test"
    assert data["status"] == "created"


def test_get_task_not_found():
    response = client.get("/tasks/invalid-id")
    assert response.status_code == 404


def test_update_task():
    created = client.post("/tasks/", json={"title": "Old", "description": "Desc"}).json()
    task_id = created["id"]

    response = client.put(f"/tasks/{task_id}", json={"title": "New", "status": "in_progress"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New"
    assert data["status"] == "in_progress"


def test_delete_task():
    created = client.post("/tasks/", json={"title": "Del", "description": "Desc"}).json()
    task_id = created["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["ok"] is True
