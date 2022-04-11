from fastapi import APIRouter, Response, status, Path, HTTPException
from pydantic import BaseModel, constr, EmailStr
import email_validator

class User(BaseModel):
    first_name: constr(min_length=2, max_length=30, strip_whitespace=True, regex=r'^[a-zA-Z]+$') | None = None
    last_name: constr(min_length=2, max_length=30, strip_whitespace=True, regex=r'^[a-zA-Z]+$') | None = None
    email: EmailStr | None = None
    username: constr(min_length=3, max_length=12, strip_whitespace=True, regex=r'^[a-zA-Z]+$') | None = None
    # class Config:
    #     extra = "forbid"

resource_data = {
  "employees": [
    {
      "first_name": "Maria",
      "last_name": "Sanchez",
      "username": "msanchez",
      "email": "maria@example.com",
      "id": 101444
    },
    {
      "first_name": "Quo",
      "last_name": "Chen",
      "username": "quochen",
      "email": "quobinchen@domain.com",
      "id": 1049832
    },
    {
      "first_name": "Danelle",
      "last_name": "Johnson",
      "username": "djohnson",
      "email": "danellej@custom.com",
      "id": 276076
    },
    {
      "first_name": "Sean",
      "last_name": "Monroe",
      "username": "seanm",
      "email": "smonroe44@social.com",
      "id": 457221
    }
  ]
}
route = APIRouter()

@route.get("/resource/", summary="Return a list of all resources", tags=["example resource"])
async def get_resource(response: Response):
    response.status_code=status.HTTP_200_OK
    return resource_data

@route.get("/resource/{id}", summary="Return a specific resource by id", tags=["example resource"])
def get_resource_id(response: Response, id: int = Path(..., title="Employee id to return.", ge=100000, le=9999999)):
    """
    Must supply a valid {id}.    
    """
    result = [x for x in resource_data['employees'] if x["id"]==id]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Employee not found"}
    response.status_code=status.HTTP_200_OK
    return result[0]

@route.post("/resource/", response_model=User, summary="Create new resource", tags=["example resource"])
def post_resource(user: User, response: Response):
    """
    Confirms the new employee username is not already in use before creating new resource.   
    """
    result = [x for x in resource_data['employees'] if x["username"]==user.username]
    if len(result) != 0:
        response.status_code=status.HTTP_403_FORBIDDEN
        return {"detail": "username is already in use."}
    if user.username == None:
        response.status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        return {"detail": "username is required."}
    new_user = user.dict()
    new_user["id"] = 509612
    return new_user

@route.put("/resource/{id}", summary="Modify all fields of an existing resource", tags=["example resource"])
def put_resource_id(user: User, response: Response, id: int = Path(..., title="Employee id to modify.", ge=100000, le=9999999)):
    """
    Put expects to replace the entire resource.  

    Will confirm that a valid {id} is supplied.  
    If no updated info is provided for a field, it will result in a Null entry.  
    """
    result = [x for x in resource_data['employees'] if x["id"]==id]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Employee not found"}
    if user.username != None:
        response.status_code=status.HTTP_403_FORBIDDEN
        return {"detail": "username may not be changed."}

    result[0]["first_name"] = user.first_name
    result[0]["last_name"] = user.last_name
    result[0]["email"] = user.email
    return result

@route.patch("/resource/{id}", summary="Modify one or more fields of existing resource", tags=["example resource"])
def patch_resource_id(user: User, response: Response, id: int = Path(..., title="Employee id to modify.", ge=100000, le=9999999)):
    """
    Patch will makle changes only for the data you supply.  

    Will confirm that a valid {id} is supplied.  
    If no updated info is provided for a field, it will not be modified.  
    """
    result = [x for x in resource_data['employees'] if x["id"]==id]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Employee not found"}
    if user.username != None:
        response.status_code=status.HTTP_403_FORBIDDEN
        return {"detail": "username may not be changed."}

    if user.first_name != None:
        result[0]["first_name"] = user.first_name
    if user.last_name != None:
        result[0]["last_name"] = user.last_name
    if user.email != None:
        result[0]["email"] = user.email
    return result[0]

@route.delete("/resource/{id}", summary="Delete a specific resource by id", tags=["example resource"])
def get_resource_id(response: Response, id: int = Path(..., title="Employee id to delete.", ge=100000, le=9999999)):
    """
    Must supply a valid {id}.    
    """
    result = [x for x in resource_data['employees'] if x["id"]==id]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Employee not found"}
    response.status_code=status.HTTP_204_NO_CONTENT
    return {}
