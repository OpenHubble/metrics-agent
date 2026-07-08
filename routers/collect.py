# FastAPI
from fastapi import APIRouter, Depends

# Middlewares
from middlewares.apikey import apikey_middleware
from middlewares.ip import ip_middleware

# Router
router = APIRouter(
    prefix="",
    tags=["Metrics"]
)


@router.get("/metrics", dependencies=[Depends(ip_middleware), Depends(apikey_middleware)])
async def metrics():
    """
    Get basic metrics of the system (CPU, memory, swap, disk IO, etc.).

    **Headers**:
    - `X-API-KEY`: The API key required for authentication.
    """

    return {"message": "Route: /api/metrics"}


@router.get("/metrics/host", dependencies=[Depends(ip_middleware), Depends(apikey_middleware)])
async def get_host_metrics():
    """
    Get detailed host metrics.

    This includes information like CPU usage, memory usage, disk IO, and network IO.

    **Headers**:
    - `X-API-KEY`: The API key required for authentication.
    """

    return {"message": "Route: /api/metrics/host"}


@router.get("/metrics/docker", dependencies=[Depends(ip_middleware), Depends(apikey_middleware)])
async def get_docker_metrics():
    """
    Get Docker container metrics.

    **Headers**:
    - `X-API-KEY`: The API key required for authentication.
    """

    return {"message": "Route: /api/metrics/docker"}
