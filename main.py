from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.db.base import init_db
from src.routers.v1.DiskRouter import disk_router
from src.routers.v1.MaterialRouter import material_router
from src.routers.v1.ScienceRouter import science_router
from src.routers.v1.ThemeRouter import theme_router
from src.routers.v1.TranscribesRouter import transcribe_router
from src.routers.v1.UserRouter import user_router
from src.routers.v1.WorkbookRouter import workbook_router

version = "v1"

description = """
A REST API for a summarize information from video
    """

version_prefix = f"/api/{version}"


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
    redoc_url=f"{version_prefix}/redoc",
)

origins = [
    "http://localhost",
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(disk_router, prefix=f"{version_prefix}/disk")
app.include_router(user_router, prefix=f"{version_prefix}/user")
app.include_router(workbook_router, prefix=f"{version_prefix}/workbook")
app.include_router(science_router, prefix=f"{version_prefix}/science")
app.include_router(transcribe_router, prefix=f"{version_prefix}/transcribe")
app.include_router(theme_router, prefix=f"{version_prefix}/theme")
app.include_router(material_router, prefix=f"{version_prefix}/material")
