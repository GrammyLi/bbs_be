import uuid
from functools import wraps

from flask import session, request, abort, jsonify

from models.user import User

# import redis
import json

def current_user():
    # print('validate_login', form, query)
    token = request.headers.get('Authorization').split(' ')[1]
    u = User.one(signature=token[:50])
    return u
 

