from fastapi.testclient import TestClient

from api.main import api
from api.config import route_prefix

client = TestClient(api)
client.base_url += route_prefix
client.base_url = client.base_url.rstrip("/") + "/"

def test_healthz():
    response = client.get("healthz")
    assert response.status_code == 200