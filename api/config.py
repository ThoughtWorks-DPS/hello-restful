"""
hello-restful api

api base configuration
"""
import os
from pydantic import BaseSettings

DESCRIPTION = """
<a href="https://github.com/ThoughtWorks-DPS/hello-restful"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/ThoughtWorks-DPS/hello-restful"></a> <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/ThoughtWorks-DPS/hello-restful"></a>
<div align="center">
	<p>
		<img alt="Thoughtworks Logo" src="https://raw.githubusercontent.com/ThoughtWorks-DPS/static/master/thoughtworks_flamingo_wave.png?sanitize=true" width=400 />
    <br />
		<img alt="DPS Title" src="https://raw.githubusercontent.com/ThoughtWorks-DPS/static/master/EMPCPlatformStarterKitsImage.png" width=350/>
	</p>
  <h1>Lightweight RESTful API simulator and testing endpoint</h1>
</div>
<br />
"""

# pylint: disable=too-few-public-methods
class Settings(BaseSettings):
    """base settings"""
    title: str = "hello-restful"
    description: str = DESCRIPTION
    prefix: str = "/hello"
    debug: bool = False
    releaseId: str = os.environ.get("API_VERSION")
    version: str = "v1"
    server_info_url: str = "http://localhost:15000/server_info"

settings = Settings()
route_prefix = f"/{settings.version}{settings.prefix}"
