# hello-restful

initial resources
## no resource
* GET / = json response { "message": "Hello Restful!"}

## status codes
* GET /status/{status code} = Returns the {status code} or 200 if none specified
* POST /status/{status code}
* PUT /status/{status code}
* PATCH /status/{status code}
* DELETE /status/{status code}




## verbs
* GET /resource = returns a simple json document of a list of records
* GET /resource/{id} = returns a simple json document with id = {id}
* POST /resource = expects json body, returns whatever you send (within validation rules)
* PUT /resource = expects json body, returns whatever you send (within validation rules)
* PATCH /resource/{id} = expects json body, returns simple json docuement that includes whatever you send (within validation rules)
* DELETE resource/{id} = returns 200 so long as you specify some {id} 

## request inspection
* GET /headers = Return the incoming request's HTTP headers.
* GET /ip = Returns the requester's IP Address.

## data respones
* GET /json = returns simple json docment
* GET /html = return simple html document
* GET /image = returns a png image


## developement

run the app for now
```
$ uvicorn api:main:app --reload