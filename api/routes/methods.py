from fastapi import APIRouter, Response, status
from pydantic import BaseModel

class User(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    username: str

my_data = {
  "users": [
    {
      "id": "101",
      "first_name": "Maria",
      "last_name": "Sanchez",
      "username": "msanchez",
      "email": "maria@example.com"
    },
    {
      "id": "104",
      "first_name": "Quo",
      "last_name": "Chen",
      "username": "quochen",
      "email": "quobinchen@domain.com"
    },
    {
      "id": "276",
      "first_name": "Danelle",
      "last_name": "Johnson",
      "username": "djohnson",
      "email": "danellej@custom.com"
    },
    {
      "id": "457",
      "first_name": "Sean",
      "last_name": "Monroe",
      "username": "seanm",
      "email": "smonroe44@social.com"
    }
  ]
}
route = APIRouter()

@route.get("/resource/", summary="Return a list of all resources", tags=["example resource"])
async def get_resource(response: Response):
    response.status_code=status.HTTP_200_OK
    return my_data

@route.get("/resource/{id}", summary="Return a specific resource by id", tags=["example resource"])
async def get_resource(response: Response, id: str):
    result = [x for x in my_data['users'] if x["id"]==id]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Resource not found"}
    else:
        response.status_code=status.HTTP_200_OK
        return result[0]

@route.post("/resource/{id}", summary="Create new resource", tags=["example resource"])
async def get_resource(response: Response, resource: ):
    result = [x for x in my_data['users'] if x["id"]==id]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Resource not found"}
    else:
        response.status_code=status.HTTP_200_OK
        return result[0]