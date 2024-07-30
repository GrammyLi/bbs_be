import time

from sqlalchemy import String, Integer, Column, Text, UnicodeText, Unicode, Boolean


from models.base_model import SQLMixin, db
from models.user import User
from models.reply import Reply


class Topic(SQLMixin, db.Model):
    views = Column(Integer, nullable=False, default=0)
    title = Column(Unicode(50), nullable=False)
    content = Column(UnicodeText, nullable=False)
    user_id = Column(Integer, nullable=False)
    board_id = Column(Integer, nullable=False)
    is_top = Column(Boolean, nullable=False, default=False)
    views =  Column(Integer, nullable=False, default=0)
    resolved = Column(Boolean, nullable=False, default=False)
    last_reply_at = Column(Integer, default=int(time.time()))

    @classmethod
    def new(cls, form, user_id):
        form['user_id'] = user_id
        form['created_time'] = int(time.time())
        form['updated_time'] = int(time.time())
        m = super().new(form)
        return m

    @classmethod
    def get(cls, id):
        m = cls.one(id=id)
        m.views += 1
        m.save()
        return m

    def user(self):
        u = User.one(id=self.user_id)
        return u
    
    def username(self):
        u = User.one(id=self.user_id)
        return u.username

    def replies(self):
        ms = Reply.all(topic_id=self.id)
        return ms

    def reply_count(self):
        count = len(self.replies())
        return count

    def reply_new(self):
        rs = Reply.all(topic_id=self.id)
        if len(rs) > 0:
            r_new = rs[-1]
            return r_new
        else:
            return self
