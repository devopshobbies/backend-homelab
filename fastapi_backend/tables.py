#### piccolo models

from datetime import datetime, timezone
from piccolo.table import Table
from piccolo.columns import (
    BigSerial,
    ForeignKey,
    Text,
    Varchar,
    Integer,
    Timestamptz,
    LazyTableReference
)
from piccolo.columns.m2m import M2M
from piccolo.columns.readable import Readable

def current_utc_timestamp():
    return datetime.now(timezone.utc)


class FavoriteMovie(Table):
    """FavoriteMovie model.
    r

    Attributes:
        id (int): Primary Key for uniquely identifying each entry.
        created_at (timestamptz): Timestamptz indicating when the entry
                                was created.
        updated_at (timestamptz): Timestamptz indicating when the entry
                                was last updated.
        name (str): Name of the movie
        poster_url (str): The URL of the movie's poster.
    """
    id = BigSerial(primary_key=True, index=True)
    name = Varchar()
    poster_url = Varchar()
    rank = Integer()