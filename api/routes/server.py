"""
hello-restful api

Return server information
"""
import json

import requests
from fastapi import APIRouter, status, Response

from api.config import settings

route = APIRouter()


@route.get("/server/locality",
           summary="Return server locality",
           tags=["server"],
           status_code=status.HTTP_200_OK
           )
async def get_server_locality(response: Response):
    """
    Returns locality of server as determined from underlying platform (assumes istio sidecar)
    """
    try:
        response.status_code = status.HTTP_200_OK
        server_response = requests.get(settings.server_info_url)
        json_response = json.loads(server_response.content)
        locality = json_response['node']['locality']
        return locality
    except requests.exceptions.ConnectionError:
        response.status_code = status.HTTP_502_BAD_GATEWAY
        return {
            "message": "Unable to query server information"
        }
