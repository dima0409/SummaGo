from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.middleware import register_middleware
from src.db.base import init_db
from src.routers.v1.DiskRouter import disk_router
from src.routers.v1.TranscribesRouter import transcribe_router

version = "v1"

description = """
A REST API for a summarize information from video
    """

version_prefix =f"/api/{version}"


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    print("Server is stopping")
app = FastAPI(
    title="SummaGo",
    description=description,
    version=version,
    lifespan=lifespan,
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)


register_middleware(app)


app.include_router(disk_router, prefix=f"{version_prefix}/disk")

app.include_router(transcribe_router, prefix=f"{version_prefix}/transcribe")




