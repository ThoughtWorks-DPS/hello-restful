from fastapi.testclient import TestClient

from api.main import api

client = TestClient(api)

def test_get_png():
    response = client.get("/png")
    assert response.status_code == 200

def test_get_html():
    response = client.get("/html")
    print(response.headers)
    assert response.status_code == 200
    #assert response.headers.content_type == "text/html"


# content-length: 653 
#  content-type: text/html; charset=utf-8 