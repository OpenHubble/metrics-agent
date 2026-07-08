# FastAPI
from fastapi import APIRouter, Depends
from pydantic import BaseModel

# Middlewares
from middlewares.apikey import apikey_middleware
from middlewares.ip import ip_middleware

# Router
router = APIRouter(
    prefix="",
    tags=["Collect"]
)


class CollectRequest(BaseModel):
    collectors: list[str] = ["cpu", "memory"]


@router.get("/collect", dependencies=[Depends(ip_middleware), Depends(apikey_middleware)])
async def collect(metrics: CollectRequest):
    """
    Collect and response to server

    **Headers**:
    - `X-API-KEY`: The API key required for authentication.

    **Body**
    ```json
    {
        "collectors.py": [
            "cpu",
            "memory",
            "docker"
        ]
    }
    ```
    """

    print(metrics)

    return {"message": "Route: /api/collect"}
