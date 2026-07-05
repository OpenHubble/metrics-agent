# IP Address
import ipaddress

# FastAPI
from fastapi import HTTPException, Request, status

# Settings
from settings import settings

# Tuple for allowed network range IPs
_ALLOWED_NETWORKS = tuple(
    ipaddress.ip_network(network)
    for network in settings.allowed_ips.split(",")
)


# IP access middleware
async def ip_middleware(request: Request):
    client_ip = ipaddress.ip_address(request.client.host)

    if not any(client_ip in network for network in _ALLOWED_NETWORKS):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Your IP is not allowed",
        )
