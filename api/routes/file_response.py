from fastapi import APIRouter, Response, status, Path
from fastapi.responses import FileResponse, HTMLResponse

# file paths
html_file = "./api/static/index.html"
png_file = "./api/static/thoughtworks_flamingo_wave.png"
mp4_video_file = "./api/static/birds.mp4"


route = APIRouter()

@route.get("/html",
                 summary="Return html file.",
                 tags=["response formats"],
                 response_class=FileResponse,
                 status_code=status.HTTP_200_OK
                 )
async def get_html():
    return html_file

@route.get("/png",
                 summary="Return png image file.",
                 tags=["response formats"],
                 response_class=FileResponse,
                 status_code=status.HTTP_200_OK
                 )
async def get_png():
    return png_file
