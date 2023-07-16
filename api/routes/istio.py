"""
hello-restful api

Return server information
"""
import json

import requests
from fastapi import APIRouter, status, Response

from api.config import settings

route = APIRouter()


@route.get("/istio/envoy",
           summary="Return envoy metadata",
           tags=["istio"],
           status_code=status.HTTP_200_OK
           )
async def get_envoy_metadata(response: Response):
    """
    Returns locality metadata queried from istio envoy sidecar
    """
    try:
        response.status_code = status.HTTP_200_OK
        server_response = requests.get(settings.server_info_url, timeout=10)
        json_response = json.loads(server_response.content)
        #locality = json_response['node']['locality']
        #return {"locality": locality}
        return json_response
    except requests.exceptions.ConnectionError:
        response.status_code = status.HTTP_502_BAD_GATEWAY
        return {
            "message": "Unable to query server information"
        }
