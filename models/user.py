import hashlib
import time

from sqlalchemy import Column, String, Integer
import config
from models.base_model import SQLMixin, db


class User(SQLMixin, db.Model):
    username = Column(String(50), nullable=False)
    password = Column(String(256), nullable=False)
    image = Column(String(100), nullable=False, default='/images/default.jpg')
    email = Column(String(50), nullable=False, default=config.test_mail)
    signature = Column(String(256), default='老李的论坛') 
    session_id = Column(String(256), nullable=False)
    role = Column(String(50), nullable=False)
    phone_number = Column(String(50), nullable=False)
    last_login = Column(Integer, default=int(time.time()))
    bio =  Column(String(50), nullable=False)


    @classmethod
    def salted_password(cls, password, salt='$!@><?>HUI&DWQa`'):
        salted = hashlib.sha256((password + salt).encode('ascii')).hexdigest()
        return salted

    @classmethod
    def register(cls, form):
        name = form.get('username', '')
        if len(name) > 2 and User.one(username=name) is None:
            form['password'] = User.salted_password(form['password'])
            u = User.new(form)
            return u
        else:
            return None

    @classmethod
    def validate_login(cls, form):
        query = dict(
            username=form['username'],
            password=User.salted_password(form['password']),
        )
        print('validate_login', form, query)
        return User.one(**query)
    
 
   
