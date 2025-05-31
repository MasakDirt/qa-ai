from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.api.v1.router import default_router


# Create the app
app = FastAPI(
    title="Q&A Service",
    servers=[
        {"url": "/", "description": "Default (Current URL)"},
        {"url": "http://localhost:3000", "description": "Local"},
    ],
    openapi_url="/api/doc/v1/docs/openapi.json",
    docs_url="/api/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

default_router(app)
