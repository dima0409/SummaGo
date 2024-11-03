from fastapi import FastAPI
from src.auth.routes import auth_router
from src.books.routes import book_router
from src.reviews.routes import review_router
from src.tags.routes import tags_router

from src.routers.v1.DiskRouter import disk_router
from src.routers.v1.TranscribesRouter import transcribe_router
from .errors import register_all_errors
from .middleware import register_middleware


version = "v1"

description = """
A REST API for a summarize information from video
    """

version_prefix =f"/api/{version}"

app = FastAPI(
    title="SummaGo",
    description=description,
    version=version,

    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)

register_all_errors(app)

register_middleware(app)


app.include_router(disk_router, prefix=f"{version_prefix}/disk")

app.include_router(transcribe_router, prefix=f"{version_prefix}/transcribe")




