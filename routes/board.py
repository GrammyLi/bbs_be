from helpers.http_helper import HTTPHelper
from helpers.errcode import ErrCode
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    jsonify,
)

from routes import *

from models.board import Board

from utils import log

main = Blueprint('board', __name__)


@main.route("/list")
def index():
    bs = Board.all()
    log("bs", bs)
    # 将每个 Board 实例转换为字典
    data = [b.to_dict() for b in bs]
    return HTTPHelper.generate_response(
        code=ErrCode.ERROR_SUCCESS,
        msg='获取成功',
        data=data
    )


@main.route("/add", methods=["POST"])
def add():
    form = request.get_json()
    log("form", form)
    u = current_user()
    # TODO v这里判断是否是管理员、或者超级管理员
    m = Board.new(form)
    return HTTPHelper.generate_response(
        code=ErrCode.ERROR_SUCCESS,
        msg='添加成功',
        data=m.to_dict()
    )


@main.route("/update", methods=["POST"])
def update():
    form = request.get_json()
    u = current_user()
    # TODO v这里判断是否是管理员、或者超级管理员
    m = Board.update(form)
    return HTTPHelper.generate_response(
        code=ErrCode.ERROR_SUCCESS,
        msg='更新成功',
        data=m.to_dict()
    )


@main.route("/remove")
def remove():
    id = request.args.get('board_id')
    form = {
        'id': id,
        'status': 0
    }
    m = Board.update(form)
    return HTTPHelper.generate_response(
        code=ErrCode.ERROR_SUCCESS,
        msg='删除成功',
        data=m.to_dict()
    )
