from typing import Annotated
from fastapi.routing import APIRouter
from fastapi_backend.tables import FavoriteMovie
from fastapi_backend.serializers import FavoriteMoviesResponse
router_main = APIRouter()

@router_main.get('/')
async def index():
    return {"message": "I'm Alive!"}


@router_main.get('/api/v1/favorite-movies')
async def get_favorite_movies():
    favorite_movies = await FavoriteMovie.select()
    return favorite_movies
