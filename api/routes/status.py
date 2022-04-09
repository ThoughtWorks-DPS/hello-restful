from fastapi import APIRouter, status, Path, Response
from pydantic import BaseModel

class Message(BaseModel):
    message: str

responses = {
    200: {"model": Message, "description": "Sucess"},
    300: {"model": Message, "description": "Redirection"},
    400: {"model": Message, "description": "Client Errors"},
    500: {"model": Message, "description": "Server Errors"}
}

route = APIRouter()

@route.api_route("/status/{code}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"], summary="Return the requested status code.", tags=["status codes"], responses={**responses})
#@route.get("/status/{code}", summary="Return the requested status code.", tags=["status codes"], responses={**responses})
def return_status(response: Response, code: int = Path(..., title="Status code to return.", ge=200, le=599)):
    response.status_code=code

    return {"code": code}
