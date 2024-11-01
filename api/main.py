from fastapi import FastAPI

from routers.v1.DiskRouter import DiskRouter

app = FastAPI()

app.include_router(DiskRouter)
