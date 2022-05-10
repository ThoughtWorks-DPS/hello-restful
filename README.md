<div align="center">
	<p>
		<img alt="Thoughtworks Logo" src="https://raw.githubusercontent.com/ThoughtWorks-DPS/static/master/thoughtworks_flamingo_wave.png?sanitize=true" width=200 />
    <br />
		<img alt="DPS Title" src="https://raw.githubusercontent.com/ThoughtWorks-DPS/static/master/dps_lab_title.png" width=350/>
	</p>
  <h3>Lightweight RESTful API simulator and testing endpoint</h3>
  <h1>hello-restful</h1>
  <a href="https://app.circleci.com/pipelines/github/ThoughtWorks-DPS/circleci-remote-docker"><img src="https://circleci.com/gh/ThoughtWorks-DPS/circleci-remote-docker.svg?style=shield"></a> <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/ThoughtWorks-DPS/circleci-remote-docker"></a>
</div>
<br />

See auto-generated fastAPI openapi documention for details.  

## local developement

**to run locally with uvicorn, not on k8s**  

```
$ uvicorn api.main:api --reload
```

Access on http://localhost/v1/hello  
OAS documentation on http://localhost/v1/hello/apidocs  

