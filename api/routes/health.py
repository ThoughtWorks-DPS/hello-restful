"""
hello-restful api

health-check endpoint.
Since hello-restful does not interact with any other services,
only a simple check is required to ensure the service is up.
"""
from datetime import datetime
from fastapi import APIRouter, status
from ..config import settings

route = APIRouter()

@route.get("/healthz/",
           summary="Simple service health check.",
           tags=["main"],
           status_code=status.HTTP_200_OK
           )
async def get_healthz():
    """
    Returns 200 if service is running.
    """
    return {
      "status": "ok",
      "version": settings.version,
      "releaseId": settings.releaseId,
      "description": "health of hello-restful service",
      "time": datetime.now().isoformat()
    }
