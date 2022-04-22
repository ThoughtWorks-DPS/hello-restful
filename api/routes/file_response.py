"""
hello-restful api

Example file response
"""
from fastapi import APIRouter, status
from fastapi.responses import FileResponse

# file paths
HTML_FILE = "./api/static/index.html"
HTML_METADATA = "./api/static/html_metadata.json"
PNG_FILE = "./api/static/thoughtworks_flamingo_wave.png"
PNG_METADATA = "./api/static/png_metadata.json"

route = APIRouter()

@route.get("/html",
                 summary="Return html file.",
                 tags=["response formats"],
                 response_class=FileResponse,
                 status_code=status.HTTP_200_OK
                 )
async def get_html():
    """Return html file."""
    return HTML_FILE

@route.get("/png",
                 summary="Return png image file.",
                 tags=["response formats"],
                 response_class=FileResponse,
                 status_code=status.HTTP_200_OK
                 )
async def get_png():
    """Return png image file."""
    return PNG_FILE

@route.get("/html/metadata",
                 summary="Return file metadata.",
                 tags=["response formats"],
                 response_class=FileResponse,
                 status_code=status.HTTP_200_OK
                 )
async def get_html_metadata():
    """Return hmtl file metadata."""
    return HTML_METADATA

@route.get("/png/metadata",
                 summary="Return file metadata.",
                 tags=["response formats"],
                 response_class=FileResponse,
                 status_code=status.HTTP_200_OK
                 )
async def get_png_metadata():
    """Return png file metadata."""
    return PNG_METADATA
