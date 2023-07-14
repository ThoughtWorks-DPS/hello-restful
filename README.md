<div align="center">
	<p>
		<img alt="Thoughtworks Logo" src="https://raw.githubusercontent.com/ThoughtWorks-DPS/static/master/thoughtworks_flamingo_wave.png?sanitize=true" width=200 />
    <br />
		<img alt="DPS Title" src="https://raw.githubusercontent.com/ThoughtWorks-DPS/static/master/dps_lab_title.png" width=350/>
	</p>
  <h3>Lightweight API providing request and response endpoints</h3>
  <h1>hello-restful</h1>
  <a href="https://app.circleci.com/pipelines/github/ThoughtWorks-DPS/hello-restful"><img src="https://circleci.com/gh/ThoughtWorks-DPS/hello-restful.svg?style=shield"></a> <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/ThoughtWorks-DPS/circleci-remote-docker"></a>
</div>
<br />

hello-restful is a lightweight api designed to be deployed on a kubernetes-based delivey infrastructure and provide common http testing endpoints and demonstrate one method of using an openapi framework for automated api documentation.  

To deploy in local cluster:  

For a simple demo of the api features and documentation: `docker run -it -d -p 8000:8000 ghcr.io/thoughtworks-dps/hello-restful`.  

## local developement  

**run locally with uvicorn**  

```
$ uvicorn api.main:api --reload
```

Access on http://localhost:8000/v1/hello  
OAS documentation on http://localhost:8000/v1/hello/apidocs  
