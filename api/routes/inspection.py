from fastapi import APIRouter, Request, status

route = APIRouter()

@route.get("/headers/", summary="Return the incoming request's HTTP headers.", tags=["request inspection"])
async def get_headers(request: Request, status_code=status.HTTP_200_OK):
    """
    Returns all information in the Starlette Request object.
    """
    return {"headers": request.headers}


@route.get("/ip/", summary="Returns the requester's IP Address.", tags=["request inspection"])
async def get_ip(request: Request, status_code=status.HTTP_200_OK):
    """
    Returns request.client.host.
    """
    return {"ip": request.client.host}

