import uuid
from functools import wraps

from flask import session, request, abort, jsonify

from models.user import User
from models.session import Session


# import redis
import json


def current_user():
    token = request.headers.get('Authorization').split(' ')[1]
    s = Session.one(token=token)
    u = User.one(id=s.user_id)
    return u
