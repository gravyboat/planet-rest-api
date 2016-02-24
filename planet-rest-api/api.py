#!usr/bin/python

from flask import Flask, jsonify, abort
from flask.ext.restful import Api, Resource, reqparse
import json


app = Flask(__name__, static_url_path="")
api = Api(app)


users = [ 
    {
        "first_name": "Joe",
        "last_name": "Smith",
        "userid": "jsmith",
        "groups": ["admins", "users"]
    },
    {
        "first_name": "Bob",
        "last_name": "Brash",
        "userid": "bbrash",
        "groups": ["admins","users"]
    }
]

class UserAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('first_name', type=str, location='json')
        self.reqparse.add_argument('last_name', type=str, location='json')
        self.reqparse.add_argument('userid', type=str, location='json')
        self.reqparse.add_argument('groups', type=list, location='json')
        super(UserAPI, self).__init__()

    def get(self, userid):
        user = [user for user in users if user['userid'] == userid]
        if len(user) == 0:
            abort(404)
        return user[0]
    
    def post(self):
        args = self.reqparse.parse_args()
        user = {
            'first_name': args['first_name'],
            'last_name': args['last_name'],
            'userid': args['userid'],
            'groups': args['groups']
        }
        for existing_user in users:
            if user['userid'] == existing_user['userid']:
                    abort(409)
        users.append(user)
        return user, 201

    def put(self, userid):
        user = [user for user in users if user['userid'] == userid]
        if len(user) == 0:
            abort(404)
        user = user[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                user[k] = v
        return user

    def delete(self, userid):
        user = [user for user in users if user['userid'] == userid]
        if len(user) == 0:
            abort(404)
        users.remove(user[0])
        return {'result': True}


class GroupAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('group', type=str, location='json')
        super(GroupAPI, self).__init__()

    def get(self, group):
        user_groups = {"userids":[]}
        userid_list = ([user["userid"] for user in users if group in user["groups"]])
        for userid in userid_list:
            user_groups["userids"].append(userid)
        print(user_groups)
        if len(user_groups) == 0:
            abort(404)
        return(user_groups)


api.add_resource(GroupAPI, '/api/v1.0/groups/<group>', endpoint='group')
api.add_resource(UserAPI, '/api/v1.0/users/<userid>', endpoint='userid')
api.add_resource(UserAPI, '/api/v1.0/users/', endpoint='user')


if __name__ == '__main__':
    app.run(debug=True)

