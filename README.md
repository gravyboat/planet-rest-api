## planet-rest-api

A simple rest api for a coding exercise.

## Installation:

#### Manual git clone

Clone the repo: `git clone https://github.com/gravyboat/planet-rest-api.git`

Create the virtualenv within the planet-rest-api directory: `virtualenv ./env; source env/bin/activate`

Install requirements: `pip install -r requirements.txt`

start the server: `python planet-rest-api/api.py`

Requests can now be made against the system as described in the [Example Usage](#example usage)

## Example Usage:

##### /users:

GET: `curl http://127.0.0.1:5000/api/v1.0/users/bbrash`

POST: `curl -H "Content-Type: application/json" -v -X POST -d '{"first_name": "roger", "last_name": "test", "userid": "rtest", "groups": ["users"]}' http://127.0.0.1:5000/api/v1.0/users/`

DELETE: `curl -v -X DELETE http://127.0.0.1:5000/api/v1.0/users/bbrash`

PUT: `curl -H "Content-Type: application/json" -v -X PUT -d '{"first_name": "roger", "userid": "rbrash"}' http://127.0.0.1:5000/api/v1.0/users/bbrash`
Note that groups used in a users PUT command will override all groups.


##### /groups:

GET: `curl http://127.0.0.1:5000/api/v1.0/groups/admins`
POST: Not implemented, group work should be associated with a user.
PUT: Not implemented, group work should be associated with a user.
DELETE: Not implemented, group work should be assocated with a user.

## Sources:

Uses https://github.com/miguelgrinberg/REST-tutorial/blob/master/rest-server-v2.py
as a base, thanks to Miguel.
