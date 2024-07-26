import time

from sqlalchemy import Unicode, Column, Integer

from models.base_model import db, SQLMixin


class Session(SQLMixin, db.Model):
    title = Column(Unicode(50), nullable=False)
    user_id = Column(Integer, nullable=False)
    expires_at = Column(Integer, nullable=False)

    

