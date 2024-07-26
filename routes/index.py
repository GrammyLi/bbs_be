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

from utils import log

main = Blueprint('index', __name__)

 
@main.route("/register", methods=['POST'])
def register():
    form = request.form.to_dict()
    # 用类函数来判断
    u = User.register(form)
    if u is None:
        return jsonify({'msg': '注册失败', "code": 201, "data": "null",  })
    return jsonify({'msg': '注册成功', "code": 200, "data": u.to_dict(),  })


@main.route("/login", methods=['POST'])
def login():
    form = request.get_json()
    u = User.validate_login(form)
    if u is None:
        return jsonify({'msg': '登录失败', "code": 201, })
    else:
        session['user_id'] = u.id
        session.permanent = True  # 设置 session 为永久
        token = create_access_token(identity=u.id)
        signature = token[:50];
        User.update(u.id,  signature=signature)
        return HTTPHelper.generate_response(
            code=ErrCode.ERROR_SUCCESS,
            msg='登录成功',
            data=u.to_dict(),
            token= str(token)
        )


@main.route('/profile')
def profile():
    u = current_user()
    return HTTPHelper.generate_response(
        code=ErrCode.ERROR_SUCCESS,
        msg='获取用户信息成功',
        data=u.to_dict()
    )

