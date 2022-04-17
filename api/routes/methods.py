from fastapi import APIRouter, Response, status, Path
from pydantic import BaseModel, constr, EmailStr
import copy

letters_plus_dash = r'^[a-zA-Z-]+$'

class UserIn(BaseModel, anystr_strip_whitespace=True, extra="forbid"):
    first_name: constr(min_length=2, max_length=30, regex=letters_plus_dash)
    last_name: constr(min_length=2, max_length=30, regex=letters_plus_dash)
    email: EmailStr
    position: constr(min_length=2, max_length=45, regex=letters_plus_dash)

class UserUpdate(BaseModel, anystr_strip_whitespace=True, extra="forbid"):
    first_name: constr(min_length=2, max_length=30, regex=letters_plus_dash) | None
    last_name: constr(min_length=2, max_length=30, regex=letters_plus_dash) | None
    email: EmailStr | None
    position: constr(min_length=3, max_length=45, regex=letters_plus_dash) | None

# simpulated database
resource_data = {
  "employees": [
    {
      "first_name": "Maria",
      "last_name": "Sanchez",
      "email": "maria@example.com",
      "position": "staff",
      "id": 101444
    },
    {
      "first_name": "Quo",
      "last_name": "Chen",
      "email": "quobinchen@domain.com",
      "position": "staff",
      "id": 1049832
    },
    {
      "first_name": "Danelle",
      "last_name": "Johnson",
      "email": "danellej@custom.com",
      "position": "manager",
      "id": 276076
    },
    {
      "first_name": "Sean",
      "last_name": "Monroe",
      "email": "smonroe44@social.com",
      "position": "staff",
      "id": 457221
    }
  ]
}

route = APIRouter()

@route.get("/resource/",
           summary="Return a list of all resources",
           tags=["example resource"],
           status_code=status.HTTP_200_OK
           )
async def get_resource():
    # response with all resources
    return resource_data


@route.get("/resource/{id}",
           summary="Return a specific resource by id",
           tags=["example resource"],
           status_code=status.HTTP_200_OK
           )
def get_resource_id(response: Response, id: int = Path(..., title="Resource id to return.", ge=100000, le=9999999)):
    """
    Must supply a valid {id}.    
    """
    # search for supplied {id} in resource_data and error if not found
    result = [x for x in resource_data['employees'] if x["id"]==id]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Resource not found"}

    # response with found set from resource_data
    return result[0]


@route.post("/resource/",
            summary="Create new resource",
            tags=["example resource"],
            status_code=status.HTTP_201_CREATED
            )
def post_resource(user: UserIn, response: Response):
    """
    Creates a new resource. Confirms the key identifying field is not already in use before creating.   
    """
    # search for supplied {id} in resource_data and error if found
    result = [x for x in resource_data['employees'] if x["email"]==user.email]
    if len(result) != 0:
        response.status_code=status.HTTP_403_FORBIDDEN
        return {"detail": "supplied email is already in use."}
    
    # mock creating new resource
    new_user = user.dict()
    new_user["id"] = 509612

    return new_user


@route.put("/resource/{id}",
           summary="Modify all fields of an existing resource",
           tags=["example resource"],
           status_code=status.HTTP_200_OK
           )
def put_resource_id(user: UserIn, response: Response, id: int = Path(..., title="Resource id to modify.", ge=100000, le=9999999)):
    """
    Put expects to replace the entire resource.  

    Will confirm that a valid {id} is supplied.  
    All fields are required for PUT.  
    """
    # search for supplied {id} in resource_data and error if not found
    # uses a deep copy to avoid modifying the original resource_data
    data_copy = copy.deepcopy(resource_data)
    result = [x for x in data_copy['employees'] if x["id"]==id]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Resource not found"}

    # replace all fields in existing resource
    result[0].update(user.dict())
    return result[0]


@route.patch("/resource/{id}",
             summary="Modify one or more fields of existing resource",
             tags=["example resource"],
             status_code=status.HTTP_200_OK
             )
def patch_resource_id(user: UserUpdate, response: Response, id: int = Path(..., title="Resource id to modify.", ge=100000, le=9999999)):
    """
    Patch will makle changes only for the data you supply.  

    Will confirm that a valid {id} is supplied.  
    If no updated info is provided for a field, it will not be modified.  
    """
    # search for supplied {id} in resource_data and error if not found
    # uses a deep copy to avoid modifying the original resource_data
    data_copy = copy.deepcopy(resource_data)
    result = [x for x in data_copy['employees'] if x["id"]==id]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Resource not found"}

    # merge changes to existing resource
    result[0].update(user.dict(exclude_unset=True))
    return result[0]


@route.delete("/resource/{id}",
              summary="Delete a specific resource by id",
              tags=["example resource"],
              status_code=status.HTTP_204_NO_CONTENT
              )
def get_resource_id(response: Response, id: int = Path(..., title="Resource id to delete.", ge=100000, le=9999999)):
    """
    Must supply a valid {id}.    
    """
    # search for supplied {id} in resource_data and error if not found
    result = [x for x in resource_data['employees'] if x["id"]==id]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Resource not found"}
    return {}
