from fastapi.testclient import TestClient

from api.main import api
from api.config import route_prefix

client = TestClient(api)
client.base_url = client.base_url.join(route_prefix.rstrip("/") + "/")


# missing format inspection tests
def test_get_png():
    response = client.get("png")
    assert response.status_code == 200


def test_get_html():
    response = client.get("html")
    print(response.headers)
    assert response.status_code == 200


# metedata inspection tests
def test_get_png_metadata():
    response = client.get("png/metadata")
    assert response.status_code == 200
    assert response.json() == {
      "file_id": "5f746133-dbd7-45e1-8c22-dfa08d54b001",
      "owner": 101444,
      "groups": ["HRAdmin"]
    }


def test_get_html_metadata():
    response = client.get("html/metadata")
    print(response.headers)
    assert response.status_code == 200
    assert response.json() == {
      "file_id": "53b4c5f8-5f49-433e-b0f6-e56383427fdf",
      "owner": 276076,
      "groups": ["HRAdmin"]
    }
