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

initial resources  

## no resource
* GET / = json response { "message": "Hello Restful!"}

## status codes
* GET /status/{status code} = Returns the status {code} or error if invalid code requested.
* POST /status/{status code}
* PUT /status/{status code}
* PATCH /status/{status code}
* DELETE /status/{status code}

## request inspection
* GET /headers = Return the incoming request's HTTP headers.
* GET /ip = Returns the requester's IP Address.

## verbs
* GET /resource = returns a simple json document of a list of records
* GET /resource/{id} = returns a simple json document, based on prpoviding a valid {id}
* POST /resource = expects json body, returns whatever you send (within validation rules)
* PUT /resource/{id} = expects json body, valid {id}, returns the resulting updated record. Expects to update the full record and if you don't send values for fields then they are replaced with Null. (within validation rules)
* PATCH /resource/{id} = expects json body, valid {id}. returns the resulting updated record. Only updates fields you provide, up to all. Where a field is not provided no change is made. (within validation rules)
* DELETE resource/{id} = returns 204 so long as you specify valid {id} 

### data respones
_for each of the pseudo file-fetch interfaces, there is meta data assumed to be associated with the stored file available on /{id}/metadata. The metadata is to enable a simple representation of file ownership and security._
* GET /json/{id} = returns simple json docment, accept any 30 char int for id though returns the same json
* GET /image/{id} = returns a png image, accept any 30 char int for id though returns the same image

{
  "file_id": "id",
  "owner": "id",
  "groups": ["group_2", "group_2"]
}

## local developement

**to run locally with uvicorn, not on k8s**  

```
$ uvicorn api.main:api --reload
```

Access on http://localhost/v1/hello  
OAS documentation on http://localhost/v1/hello/apidocs  

