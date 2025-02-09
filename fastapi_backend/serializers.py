#### pydantic models

from typing import Optional
from pydantic import BaseModel


class FavoriteMovieResponse(BaseModel):
    id: int
    name: str
    image_url: str
    rank: int

class FavoriteMoviesResponse(BaseModel):
    result: list[FavoriteMovieResponse]
