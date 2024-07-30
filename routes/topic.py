from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    jsonify,
)
from helpers.errcode import ErrCode
from helpers.http_helper import HTTPHelper

from routes import *
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from models.board import Board
from models.topic import Topic

from . import current_user  # 使用相对导入

# import redis


main = Blueprint('topic', __name__)
# TODO:  话题全部列表缓存
# cache = redis.StrictRedis()


def get_topic_with_username(topic):
    topic_dict = topic.to_dict()
    topic_dict['username'] = topic.username()
    return topic_dict


@main.route('/list')
def index():
    board_id = int(request.args.get('board_id', -1))
    pg = int(request.args.get('pg', 1))  # 默认第1页
    sz = int(request.args.get('sz', 10))  # 默认每页10条记录
    if board_id == -1:
        total, topics = Topic.paginate(pg, sz)
    else:
        total, topics = Topic.paginate(pg, sz, board_id=board_id)
    topics_dict = [get_topic_with_username(topic) for topic in topics]
    return HTTPHelper.generate_response(
        code=ErrCode.ERROR_SUCCESS,
        msg='获取成功',
        data=topics_dict
    )


@main.route('/detail')
def detail():
    id = request.args.get('topic_id', -1)
    topic = Topic.get(id)
    if topic:
        topic_dict = get_topic_with_username(topic)
        return HTTPHelper.generate_response(
            code=ErrCode.ERROR_SUCCESS,
            msg='获取成功',
            data=topic_dict
        )
    else:
        return HTTPHelper.generate_response(
            code=ErrCode.ERROR_SUCCESS,
            msg='没有话题',
            data={}
        )


@main.route("/add", methods=["POST"])
def add():
    form = request.get_json()
    u = current_user()
    m = Topic.new(form, user_id=u.id)
    return HTTPHelper.generate_response(
        code=ErrCode.ERROR_SUCCESS,
        msg='获取成功',
        data=m.to_dict()
    )
