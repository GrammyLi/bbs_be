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


main = Blueprint('board', __name__)


@main.route("/all")
def index():
    bs = Board.all()
    print("bs", bs)
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
    print("form", form)
    u = current_user()
    m = Board.new(form)
    return jsonify({'msg': '添加成功', "code": 200, "data": m.to_dict()})

