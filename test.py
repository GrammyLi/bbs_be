from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import time
import os

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'test.sqlite3')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止修改跟踪
db = SQLAlchemy(app)


def timestamp():
    return int(time.time())


class ModelMixin(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0}=({1})'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}:\n\t{1}\n>'.format(class_name, '\n\t'.join(properties))

    def save(self):
        with app.app_context():  # 确保操作在应用程序上下文中进行
            db.session.add(self)
            db.session.commit()
        return self

    def delete(self):
        with app.app_context():
            db.session.delete(self)
            db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        with app.app_context():
            return cls.query.get(id)


class User(db.Model, ModelMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)


def db_init():
    print("1212")
    with app.app_context():
        db.create_all()


def add_one():
    with app.app_context():
        u = User()
        u.username = 'grammyli'
        u.save() 

def find_one():
    with app.app_context():
        u2 = User.find_by_id(1)  # 示例: 查找 ID 为 1 的用户
        print(u2, u2.username)


def main():
    db_init()
    add_one()
    find_one()


if __name__ == '__main__':
    main()
