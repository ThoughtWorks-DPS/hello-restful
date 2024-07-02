from fastapi.testclient import TestClient

from api.main import api
from api.config import route_prefix

client = TestClient(api)
client.base_url = client.base_url.join(route_prefix.rstrip("/") + "/")


def test_resource_get():
    response = client.get("resource")
    assert response.status_code == 200
    assert response.json() == {
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


def test_resource_get_search_with_results():
    response = client.get("resource?last_name=San")
    assert response.status_code == 200
    assert response.json() == {
      "employees": [
        {
          "first_name": "Maria",
          "last_name": "Sanchez",
          "email": "maria@example.com",
          "position": "staff",
          "userid": 101444
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


def test_resource_get_search_with_no_results():
    response = client.get("resource?last_name=West")
    assert response.status_code == 404
    assert response.json() == { "message": "no search results" }


def test_resource_get_valid_id():
    response = client.get("resource/101444")
    assert response.status_code == 200
    assert response.json() == {
      "first_name": "Maria",
      "last_name": "Sanchez",
      "email": "maria@example.com",
      "position": "staff",
      "userid": 101444
    }


def test_resource_get_invalid_id():
    response = client.get("resource/101000")
    assert response.status_code == 404
    assert response.json() == { "detail": "Resource not found" }


def test_resource_post_unique_email():
    response = client.post("resource",
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
      "userid": 509612
    }


def test_resource_post_duplicate_email():
    response = client.post("resource",
                           json={
                            "first_name": "foo",
                            "last_name": "bar",
                            "email": "maria@example.com",
                            "position": "staff"
                           })
    assert response.status_code == 403
    assert response.json() == {"detail": "supplied email is already in use."}


# post: include fields in json payload that are not in the schema
def test_resource_post_extra_data():
    response = client.post("resource",
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
    response = client.post("resource",
                           json={
                            "first_name": "foo",
                            "last_name": "bar",
                            "email": "foo@example.com"
                           })
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "input": {
                    "email": "foo@example.com",
                    "first_name": "foo",
                    "last_name": "bar"
                },
                "loc": [
                    "body",
                    "position"
                ],
                "msg": "Field required",
                "type": "missing"
            }
        ]
    }

test_resource_post_extra_data
# test model validators
def test_resource_post_model_validators():
    response = client.post("resource",
                          json={
                            "first_name": "thishastoomanycharactersthishastoomanycharacters",
                            "last_name": "a",
                            "email": "foo@example",
                            "position": "thishastoomanycharactersthishastoomanycharacters"
                          })
    assert response.status_code == 422
    print(response.json())
    assert response.json() == {
        "detail": [
            {
                "ctx": {
                    "max_length": 30
                },
                "input": "thishastoomanycharactersthishastoomanycharacters",
                "loc": [
                    "body",
                    "first_name"
                ],
                "msg": "String should have at most 30 characters",
                "type": "string_too_long"
            },
            {
                "ctx": {
                    "min_length": 2
                },
                "input": "a",
                "loc": [
                    "body",
                    "last_name"
                ],
                "msg": "String should have at least 2 characters",
                "type": "string_too_short"
            },
            {
                "ctx": {
                    "reason": "The part after the @-sign is not valid. It "
                              "should have a period."
                },
                "input": "foo@example",
                "loc": [
                    "body",
                    "email"
                ],
                "msg": "value is not a valid email address: The part after the "
                       "@-sign is not valid. It should have a period.",
                "type": "value_error"
            },
            {
                "ctx": {
                    "max_length": 45
                },
                "input": "thishastoomanycharactersthishastoomanycharacters",
                "loc": [
                    "body",
                    "position"
                ],
                "msg": "String should have at most 45 characters",
                "type": "string_too_long"
            }
        ]
    }


def test_resource_put_valid_id():
    response = client.put("resource/101444",
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
      "userid": 101444
    }


def test_resource_put_invalid_id():
    response = client.put("resource/101400",
                          json={
                            "first_name": "foo",
                            "last_name": "bar",
                            "email": "foo@example.com",
                            "position": "staff"
                          })
    assert response.status_code == 404
    assert response.json() == {"detail": "Resource not found"}


# put: fail to include required fields, include extra fields in json payload
def test_resource_put_extra_and_missing_fields():
    response = client.put("resource/101444",
                          json={
                            "last_name": "bar",
                            "email": "foo@example.com",
                            "extra": "extra data"
                          })
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "input": {
                    "email": "foo@example.com",
                    "extra": "extra data",
                    "last_name": "bar"
                },
                "loc": [
                    "body",
                    "first_name"
                ],
                "msg": "Field required",
                "type": "missing"
            },
            {
                "input": {
                    "email": "foo@example.com",
                    "extra": "extra data",
                    "last_name": "bar"
                },
                "loc": [
                    "body",
                    "position"
                ],
                "msg": "Field required",
                "type": "missing"
            },
            {
                "input": "extra data",
                "loc": [
                    "body",
                    "extra"
                ],
                "msg": "Extra inputs are not permitted",
                "type": "extra_forbidden"
            }
        ]
    }


def test_resource_patch_valid_id():
    response = client.patch("resource/101444",
                            json={
                              "position": "manager"
                            })
    assert response.status_code == 200
    assert response.json() == {
      "first_name": "Maria",
      "last_name": "Sanchez",
      "email": "maria@example.com",
      "position": "manager",
      "userid": 101444
    }


def test_resource_patch_invalid_id():
    response = client.patch("resource/101400",
                            json={
                              "position": "manager"
                            })
    assert response.status_code == 404
    assert response.json() == {"detail": "Resource not found"}


# patch:  include fields in json payload that are not in the schema
def test_resource_patch_extra_data():
    response = client.patch("resource/101444",
                            json={
                              "position": "manager",
                              "extra": "some extra data"
                          })
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "input": "some extra data",
                "loc": [
                    "body",
                    "extra"
                ],
                "msg": "Extra inputs are not permitted",
                "type": "extra_forbidden"
            }
        ]
    }


def test_resource_delete_valid_id():
    response = client.delete("resource/101444")
    assert response.status_code == 204
    assert response.content == b''


def test_resource_delete_invalid_id():
    response = client.delete("resource/101400")
    assert response.status_code == 404
    assert response.json() == {"detail": "Resource not found"}
