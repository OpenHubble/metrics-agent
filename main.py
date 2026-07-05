# FastAPI
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

# Router
from routers import agent, metric
# Config
from settings import settings

# Init FastAPI app
app = FastAPI(
    title="OpenHubble Agent",
    version=settings.project_version,
    summary="OpenHubble Agent API Documentation",
    description="API for retrieving various system and Docker metrics. Secure access requires an API key via the X-API-KEY header.",
    contact={
        "name": "OpenHubble Agent Team",
        "url": "https://openhubble.com/agent",
        "email": "agent@openhubble.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://github.com/OpenHubble/agent/blob/main/LICENSE",
    },
    openapi_tags=[
        {"name": "Agent", "description": "Base routers of Agent"},
        {"name": "Metrics", "description": "Operations related to system metrics"},
    ]
)

# Use GZIP to compress data
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)

# Include Router
app.include_router(agent.router, prefix="/api")
app.include_router(metric.router, prefix="/api")
