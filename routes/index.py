import os
import uuid
# from werkzeug.datastructures import FileStorage
from helpers.http_helper import HTTPHelper
from helpers.errcode import ErrCode
from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    abort,
    send_from_directory,
    flash,
    jsonify,
    make_response,
)
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


from routes import *

from models.user import User
from models.session import Session

from utils import log

main = Blueprint('user', __name__)

# def admin_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         user_id = get_jwt_identity()
#         user = User.get(user_id)
#         if user is None or not (user.is_admin() or user.is_super_admin()):
#             return HTTPHelper.generate_response(
#                 code=ErrCode.ERROR_AUTHORIZATION_REQUIRED,
#                 msg='只有管理员或超级管理员才能执行此操作',
#             )
#         return fn(*args, **kwargs)
#     return wrapper


@main.route("/register", methods=['POST'])
def register():
    form = request.form.to_dict()
    log("form", form)
    u = User.register(form)
    if u is None:
        return HTTPHelper.generate_response(
            code=ErrCode.ERROR_USER_NOT_EXISTS,
            msg='注册失败',
        )
    return HTTPHelper.generate_response(
        code=ErrCode.ERROR_SUCCESS,
        msg='成功',
        data=u.to_dict()
    )


@main.route("/login", methods=['POST'])
def login():
    form = request.get_json()
    u = User.validate_login(form)
    if u is None:
        return HTTPHelper.generate_response(
            code=ErrCode.ERROR_USER_NOT_EXISTS,
            msg='登录失败',
        )
    else:
        token = create_access_token(identity=u.id)
        log("token", token)
        Session.new(token=token, user_id=u.id)
        return HTTPHelper.generate_response(
            code=ErrCode.ERROR_SUCCESS,
            msg='登录成功',
            data=u.to_dict(),
            token=str(token)
        )


@main.route('/profile')
def profile():
    u = current_user()
    return HTTPHelper.generate_response(
        code=ErrCode.ERROR_SUCCESS,
        msg='获取用户信息成功',
        data=u.to_dict()
    )


@main.route('/detail')
def detail():
    u = current_user()
    if not u.is_admin() and not u.is_super_admin():
        return HTTPHelper.generate_response(
            code=ErrCode.ERROR_AUTHORIZATION_REQUIRED,
            msg='只有管理员或超级管理员才能查看用户详情',
        )
    id = request.args.get('user_id')
    user = User.get(id)
    return HTTPHelper.generate_response(
        code=ErrCode.ERROR_SUCCESS,
        msg='获取用户信息成功',
        data=user.to_dict()
    )


@main.route("/update", methods=["POST"])
def update():
    form = request.get_json()
    u = current_user()
    if not u.is_admin() and not u.is_super_admin():
        return HTTPHelper.generate_response(
            code=ErrCode.ERROR_AUTHORIZATION_REQUIRED,
            msg='只有管理员或超级管理员才能查看用户详情',
        )
    user = User.update(u.id, **form)
    return HTTPHelper.generate_response(
        code=ErrCode.ERROR_SUCCESS,
        msg='获取用户信息成功',
        data=user.to_dict()
    )
