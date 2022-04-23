"""
hello-restful api

Example http status code responses
"""
from fastapi import APIRouter, Path, Response
from pydantic import BaseModel

# pylint: disable=too-few-public-methods
class Message(BaseModel):
    """schema for message"""
    message: str

responses = {
    200: {"model": Message, "description": "Sucess"},
    300: {"model": Message, "description": "Redirection"},
    400: {"model": Message, "description": "Client Errors"},
    500: {"model": Message, "description": "Server Errors"}
}

route = APIRouter()

@route.api_route("/status/{code}",
                 methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
                 summary="Return the requested status code.",
                 tags=["status codes"],
                 responses={**responses}
                 )
def return_status(response: Response,
                  code: int = Path(...,
                                   title="Status code to return.",
                                   ge=200,
                                   le=599
                                  )
                 ):
    """Return the requested status code."""
    response.status_code=code
    return { "code": code }
