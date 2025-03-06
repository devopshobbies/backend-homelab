from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from piccolo_admin.endpoints import create_admin
from starlette.routing import Route, Mount
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from piccolo.engine import engine_finder
from fastapi_backend.piccolo_app import APP_CONFIG
from fastapi_backend.routes import router_main
from piccolo.apps.user.tables import BaseUser

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Code
    engine = engine_finder()
    await engine.start_connection_pool()

    # create admin user
    print("checking if admin user_exsits")
    admin_user = await BaseUser.select(BaseUser.username).where(BaseUser.username == 'admin')
    if len(admin_user) == 0 :
        print("created admin user.👍")
        print("use the credentials below to access the admin panel:")
        print("user: admin  ---  password: admin123456")
        await BaseUser.create_user(username="admin", password="admin123456", active=True, superuser=True, admin=True)
    else:
        print("admin user exists. skipping admin user creation...")
    

    yield

    # Graceful Shutdown Code
    engine = engine_finder()
    await engine.close_connection_pool()


app = FastAPI(
    routes=[
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG.table_classes,
                # Required when running under HTTPS:
                allowed_hosts=["localhost"],
                production=True,
            ),
        ),
    ],
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_main)