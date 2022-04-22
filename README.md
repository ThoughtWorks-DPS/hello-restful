# hello-restful

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

run the app locally (not as container)
```
$ uvicorn api.main:api --reload
```