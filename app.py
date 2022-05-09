from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.jornada import ujornada
from routers.jornada import tjornadas
from routers.jornada import ttablageneral
from routers.jornada import tproximajornada
from routers.jornada import tjugadores

from config.openapi import tags_metadata

app = FastAPI(
    title="Soccer API",
    description="a REST API Soccer",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

origins = [
    "http://187.190.159.87:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ujornada)
app.include_router(tjornadas)
app.include_router(ttablageneral)
app.include_router(tproximajornada)
app.include_router(tjugadores)
