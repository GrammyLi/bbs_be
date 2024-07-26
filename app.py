#!/usr/bin/env python3
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from datetime import timedelta

import config
from models.base_model import db

from routes.index import main as index_routes
from routes.topic import main as topic_routes
from routes.reply import main as reply_routes
from routes.board import main as board_routes
from datetime import timedelta


jwt = JWTManager()


def configured_app():
    app = Flask(__name__)
    jwt.init_app(app)
    app.secret_key = "1212"
     # Enable CORS for the app
  
    import os
    db_path = os.path.join(os.path.dirname(__file__), 'test.sqlite3')
    uri  = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
    db.init_app(app)

    register_routes(app)
    return app


def register_routes(app):
    """
    在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
    蓝图可以拥有自己的静态资源路径、模板路径
    用法如下
    """
    # 注册蓝图
    app.register_blueprint(index_routes)
    app.register_blueprint(topic_routes, url_prefix='/topic')
    app.register_blueprint(reply_routes, url_prefix='/reply')
    app.register_blueprint(board_routes, url_prefix='/board')


# 运行代码
if __name__ == '__main__':
    app = configured_app()
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    app.jinja_env.auto_reload = True
    CORS(app, resources={r"/*": {"origins": "*"}})
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
        threaded=True,
    )
    app.run(**config)
