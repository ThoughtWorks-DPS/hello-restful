
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id: int}



# in the below, you can see where specific 'users' can be reserved words, the reserved must come first
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# below would be: http://127.0.0.1:8000/items/?skip=0&limit=10
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


#optional path parameters
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# how to include 'body'

from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

#
# {
#     "name": "Foo",
#     "description": "An optional description",
#     "price": 45.2,
#     "tax": 3.5
# }

# since description and tax are optional the default value is:
# {
#     "name": "Foo",
#     "price": 45.2
# }

@app.post("/items/")
async def create_item(item: Item):
    return item


# FastAPI will recognize that the function parameters that match path parameters should be
# taken from the path, and that function parameters that are declared to be Pydantic models should be
# taken from the request body.

# the below has body, path and query parameters
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

# to access header information
from fastapi import FastAPI, Header

@app.get("/items/")
async def read_items(user_agent: str | None = Header(None)):
    return {"User-Agent": user_agent}

# status codes; in this case 201=created
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

# but I don't have to use numbers I can use the FastAPI constants
from fastapi import FastAPI, status
@app.post("/items/", status_code=status.HTTP_201_CREATED)

# returning ERRORS 400-499
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
# and the response body:
# {
#   "detail": "Item not found"
# }

# this one injects a custom header in the response
@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}




# to add formatting to docs

# this one will group all the tag paths together in the documentstion
@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


# in this one: 'summary' addes description after the path in the docs and
# the docdstring will be in the space below when you expand it
@app.post("/items/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

# after you try it, the reponsse in the doc an be labeled
@app.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    response_description="The created item",
)

# for when a path remains in service but is deprecated
@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]