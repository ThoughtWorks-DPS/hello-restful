from fastapi.testclient import TestClient

from api.main import api

client = TestClient(api)

def test_resource_get():
    response = client.get("/resource")
    assert response.status_code == 200
    assert response.json() == {
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

def test_resource_get_valid_id():
    response = client.get("/resource/101444")
    assert response.status_code == 200
    assert response.json() == {
      "first_name": "Maria",
      "last_name": "Sanchez",
      "email": "maria@example.com",
      "position": "staff",
      "id": 101444
    }

def test_resource_get_invalid_id():
    response = client.get("/resource/101000")
    assert response.status_code == 404
    assert response.json() == { "detail": "Resource not found" }

def test_resource_post():
    response = client.post("/resource/",
                            json={
                            "first_name": "foo",
                            "last_name": "bar",
                            "email": "foo@example.com",
                            "position": "staff"
                          })
    assert response.status_code == 201
    assert response.json() == {
      "first_name": "foo",
      "last_name": "bar",
      "email": "foo@example.com",
      "position": "staff",
      "id": 509612
    }

# post: include fields in json payload that are not in the schema
def test_resource_post_extra_data():
    response = client.post("/resource/",
                            json={
                            "first_name": "foo",
                            "last_name": "bar",
                            "email": "foo@example.com",
                            "position": "staff",
                            "extra": "some extra data"
                          })
    assert response.status_code == 422
    assert response.json() == {
      "detail": [
        {
          "loc": [
            "body",
            "extra"
          ],
          "msg": "extra fields not permitted",
          "type": "value_error.extra"
        }
      ]
    }

# post: fail to include all required fields in json payload
def test_resource_post_extra_data():
    response = client.post("/resource/",
                            json={
                            "first_name": "foo",
                            "last_name": "bar",
                            "email": "foo@example.com"
                          })
    assert response.status_code == 422
    assert response.json() == {
      "detail": [
        {
          "loc": [
            "body",
            "position"
          ],
          "msg": "field required",
          "type": "value_error.missing"
        }
      ]
    }

# test model validators
def test_resource_post_model_validators():
    response = client.post("/resource/",
                            json={
                            "first_name": "thishastoomanycharactersthishastoomanycharacters",
                            "last_name": "a",
                            "email": "foo@example",
                            "position": "thishastoomanycharactersthishastoomanycharacters"
                          })
    assert response.status_code == 422
    assert response.json() == {
      "detail": [
        {
          "loc": [
            "body",
            "first_name"
          ],
          "msg": "ensure this value has at most 30 characters",
          "type": "value_error.any_str.max_length",
          "ctx": {
            "limit_value": 30
          }
        },
        {
          "loc": [
            "body",
            "last_name"
          ],
          "msg": "ensure this value has at least 2 characters",
          "type": "value_error.any_str.min_length",
          "ctx": {
            "limit_value": 2
          }
        },
        {
          "loc": [
            "body",
            "email"
          ],
          "msg": "value is not a valid email address",
          "type": "value_error.email"
        },
        {
          "loc": [
            "body",
            "position"
          ],
          "msg": "ensure this value has at most 45 characters",
          "type": "value_error.any_str.max_length",
          "ctx": {
            "limit_value": 45
          }
        }
      ]
    }

def test_resource_put():
    response = client.put("/resource/101444",
                            json={
                            "first_name": "foo",
                            "last_name": "bar",
                            "email": "foo@example.com",
                            "position": "staff"
                          })
    assert response.status_code == 200
    assert response.json() == {
      "first_name": "foo",
      "last_name": "bar",
      "email": "foo@example.com",
      "position": "staff",
      "id": 101444
    }

# put: fail to include required fields, include extra fields in json payload
def test_resource_put_extra_and_missing_fields():
    response = client.put("/resource/101444",
                            json={
                            "last_name": "bar",
                            "email": "foo@example.com",
                            "extra": "extra data"
                          })
    assert response.status_code == 422
    assert response.json() == {
      "detail": [
        {
          "loc": [
            "body",
            "first_name"
          ],
          "msg": "field required",
          "type": "value_error.missing"
        },
        {
          "loc": [
            "body",
            "position"
          ],
          "msg": "field required",
          "type": "value_error.missing"
        },
        {
          "loc": [
            "body",
            "extra"
          ],
          "msg": "extra fields not permitted",
          "type": "value_error.extra"
        }
      ]
    }

def test_resource_patch():
    response = client.patch("/resource/101444",
                            json={
                            "position": "manager"
                          })
    assert response.status_code == 200
    assert response.json() == {
      "first_name": "Maria",
      "last_name": "Sanchez",
      "email": "maria@example.com",
      "position": "manager",
      "id": 101444
    }

# patch:  include fields in json payload that are not in the schema
def test_resource_patch_extra_data():
    response = client.patch("/resource/101444",
                            json={
                            "position": "manager",
                            "extra": "some extra data"
                          })
    assert response.status_code == 422
    assert response.json() == {
      "detail": [
        {
          "loc": [
            "body",
            "extra"
          ],
          "msg": "extra fields not permitted",
          "type": "value_error.extra"
        }
      ]
    }

def test_resource_delete():
    response = client.delete("/resource/101444")
    assert response.status_code == 204
    assert response.json() == {}