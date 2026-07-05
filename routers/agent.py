# FastAPI
from fastapi import APIRouter, Depends

# Middlewares
from middlewares.apikey import apikey_middleware
from middlewares.ip import ip_middleware

# Router
router = APIRouter(
    prefix="",
    tags=["Agent"]
)


@router.get("")
async def root():
    return {"message": "Route: /api"}


@router.get("/ping", dependencies=[Depends(ip_middleware), Depends(apikey_middleware)])
async def ping():
    """
    Ping the API to check if it's live.

    This endpoint checks the health of the server.

    **Headers**:
    - `X-API-KEY`: The API key required for authentication.
    """

    return {"message": "Route: /api/ping"}
