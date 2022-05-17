"""
hello-restful api

Example /resource methods
"""
import copy
from typing import Optional
from fastapi import APIRouter, Response, status, Path
from pydantic import BaseModel, constr, EmailStr, Field

LETTERS_PLUS_DASH = r'^[a-zA-Z-]+$'

# pylint: disable=too-few-public-methods
class UserIn(BaseModel, anystr_strip_whitespace=True, extra="forbid"):
    """schema for create-user input body"""
    first_name: constr(min_length=2, max_length=30, regex=LETTERS_PLUS_DASH)
    last_name: constr(min_length=2, max_length=30, regex=LETTERS_PLUS_DASH)
    email: EmailStr
    position: constr(min_length=2, max_length=45, regex=LETTERS_PLUS_DASH)

# pylint: disable=too-few-public-methods
class UserUpdate(BaseModel, anystr_strip_whitespace=True, extra="forbid"):
    """schema for update-user input body"""
    first_name: Optional[str] = Field(None, min_length=2, max_length=30, regex=LETTERS_PLUS_DASH)
    last_name: Optional[str] = Field(None, min_length=2, max_length=30, regex=LETTERS_PLUS_DASH)
    email: Optional[EmailStr]
    position: Optional[str] = Field(None, min_length=3, max_length=45, regex=LETTERS_PLUS_DASH)

# simulated database
resource_data = {
    "employees": [
        {
            "first_name": "Maria",
            "last_name": "Sanchez",
            "email": "maria@example.com",
            "position": "staff",
            "userid": 101444
        },
        {
            "first_name": "Quo",
            "last_name": "Chen",
            "email": "quobinchen@domain.com",
            "position": "staff",
            "userid": 1049832
        },
        {
            "first_name": "Danelle",
            "last_name": "Johnson",
            "email": "danellej@custom.com",
            "position": "manager",
            "userid": 276076
        },
        {
            "first_name": "Pete",
            "last_name": "Santos",
            "email": "psantos44@social.com",
            "position": "staff",
            "userid": 457221
        }
    ]
}

route = APIRouter()

@route.get("/resource",
           summary="Return a list of all resources",
           tags=["example resource"],
           status_code=status.HTTP_200_OK
           )
async def get_resource(response: Response, last_name: Optional[str] = None):
    """Return all resources or search for matching last names"""
    if last_name:
        results = search_query(last_name) # pylint: disable=too-many-function-args
        if results["employees"]:
            response.status_code = status.HTTP_200_OK
            return results
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "no search results" }

    # response with all resources
    return resource_data

@route.get("/resource/{userid}",
           summary="Return a specific resource by userid",
           tags=["example resource"],
           status_code=status.HTTP_200_OK
           )
def get_resource_userid(response: Response,
                        userid: int = Path(...,
                                           title="Resource userid to return.",
                                           ge=100000,
                                           le=9999999
                                          )
                       ):
    """
    Must supply a valid {userid}.
    """
    # search for supplied {userid} in resource_data and error if not found
    result = [x for x in resource_data['employees'] if x["userid"]==userid]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Resource not found"}

    # response with found set from resource_data
    return result[0]

@route.post("/resource",
            summary="Create new resource",
            tags=["example resource"],
            status_code=status.HTTP_201_CREATED
            )
def post_resource(user: UserIn, response: Response):
    """
    Creates a new resource. Confirms the key identifying field is not already
    in use before creating.
    """
    # search for supplied {userid} in resource_data and error if found
    result = [x for x in resource_data['employees'] if x["email"]==user.email]
    if len(result) != 0:
        response.status_code=status.HTTP_403_FORBIDDEN
        return { "detail": "supplied email is already in use." }

    # mock creating new resource
    new_user = user.dict()
    new_user["userid"] = 509612

    return new_user

@route.put("/resource/{userid}",
           summary="Modify all fields of an existing resource",
           tags=["example resource"],
           status_code=status.HTTP_200_OK
           )
def put_resource_userid(user: UserIn, response: Response,
                        userid: int = Path(...,
                                           title="Resource userid to modify.",
                                           ge=100000,
                                           le=9999999
                                          )
                       ):
    """
    Put expects to replace the entire resource.

    Will confirm that a valid {userid} is supplied.
    All fields are required for PUT.
    """
    # search for supplied {userid} in resource_data and error if not found
    # uses a deep copy to avoid modifying the original resource_data
    data_copy = copy.deepcopy(resource_data)
    result = [x for x in data_copy['employees'] if x["userid"]==userid]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return { "detail": "Resource not found" }

    # replace all fields in existing resource
    result[0].update(user.dict())
    return result[0]

@route.patch("/resource/{userid}",
             summary="Modify one or more fields of existing resource",
             tags=["example resource"],
             status_code=status.HTTP_200_OK
             )
def patch_resource_userid(user: UserUpdate, response: Response,
                          userid: int = Path(...,
                                             title="Resource userid to modify.",
                                             ge=100000,
                                             le=9999999
                                            )
                         ):
    """
    Patch will makle changes only for the data you supply.

    Will confirm that a valid {userid} is supplied.
    If no updated info is provided for a field, it will not be modified.
    """
    # search for supplied {userid} in resource_data and error if not found
    # uses a deep copy to avoid modifying the original resource_data
    data_copy = copy.deepcopy(resource_data)
    result = [x for x in data_copy['employees'] if x["userid"]==userid]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return { "detail": "Resource not found" }

    # merge changes to existing resource
    result[0].update(user.dict(exclude_unset=True))
    return result[0]

@route.delete("/resource/{userid}",
              summary="Delete a specific resource by userid",
              tags=["example resource"],
              status_code=status.HTTP_204_NO_CONTENT
              )
def delete_resource_userid(response: Response,
                        userid: int = Path(...,
                                           title="Resource userid to delete.",
                                           ge=100000,
                                           le=999999
                                          )
                       ):
    """
    Must supply a valid {userid}.
    """
    # search for supplied {userid} in resource_data and error if not found
    result = [x for x in resource_data['employees'] if x["userid"]==userid]
    if len(result) == 0:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": "Resource not found"}
    return {}

def search_query(last_name):
    """very basic search query"""
    matching = {
        "employees": []
    }

    for user in resource_data["employees"]:
        if user["last_name"].find(last_name) != -1:
            matching["employees"].append(user)
            # matching.update(user)
    return matching
