
from fastapi_backend.main import app
from fastapi.testclient import TestClient
from fastapi_backend.tables import FavoriteMovie
import json
client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "I'm Alive!"}

def test_index():
    response = client.get("/api/v1/favorite-movies")
    assert response.status_code == 200
    
    favorite_movies_db = FavoriteMovie.select().run_sync()
    assert response.json() == favorite_movies_db