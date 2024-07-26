from flask import (
    request,
    redirect,
    url_for,
    Blueprint,
    jsonify,
)

from routes import current_user

from models.reply import Reply
# from models.message import Messages
from models.user import User

main = Blueprint('reply', __name__)

def get_reply_with_username(reply):
    reply_dict = reply.to_dict()
    user = reply.user()
    reply_dict['username'] = user.username if user else 'Unknown'
    return reply_dict

@main.route("/add", methods=["POST"])
def add():
    form = request.get_json()
    u = current_user()
    m = Reply.new(form, user_id=u.id)
    return jsonify({'msg': '成功', "code": 200, "data": m.to_dict()})



@main.route("/all")
def all():
    id = request.args.get('topic_id', -1)
    replys = Reply.all(topic_id=id)
    replys_dict = [get_reply_with_username(reply) for reply in replys]
    replys_dict = sorted(replys_dict, key=lambda r: r['created_time'], reverse=True)
    return jsonify({'msg': '回复获取成功', "code": 200, "data": replys_dict})

   
