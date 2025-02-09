from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry
from piccolo_conf import *  # noqa

from dotenv import dotenv_values
import os

config = {
    **dotenv_values(".env"),   # to read development files
    **os.environ, # to read runtime environment variables
}


DB = PostgresEngine(
    config={
        "database": config["POSTGRES_DB"],
        "user": config["POSTGRES_USER"],
        "password": config["POSTGRES_PASSWORD"],
        "host": config["POSTGRES_HOST"],
        "port": config["POSTGRES_PORT"],
    }
)


APP_REGISTRY = AppRegistry(
    apps=['fastapi_backend.piccolo_app', 'piccolo_admin.piccolo_app']
)
