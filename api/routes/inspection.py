"""
hello-restful api

Example header inspection
"""
from fastapi import APIRouter, Request, status

route = APIRouter()

@route.get("/headers/",
           summary="Return the incoming request's HTTP headers.",
           tags=["request inspection"],
           status_code=status.HTTP_200_OK
           )
async def get_headers(request: Request):
    """
    Returns all information in the Starlette Request object.
    """
    return {"headers": request.headers}

@route.get("/ip/",
           summary="Returns the requester's IP Address.",
           tags=["request inspection"],
           status_code=status.HTTP_200_OK
           )
async def get_ip(request: Request):
    """
    Returns request.client.host.
    """
    return {"ip": request.client.host}
