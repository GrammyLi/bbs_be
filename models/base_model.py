import time

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class SQLMixin(object):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ct = Column(Integer, default=int(time.time()))
    ut = Column(Integer, default=int(time.time()))
    status = Column(Integer, default=int(1))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


    @classmethod
    def new(cls, form):
        m = cls()
        for name, value in form.items():
            setattr(m, name, value)

        m.save()

        return m

    @classmethod
    def update(cls, id, **kwargs):
        m = cls.query.filter_by(id=id).first()
        for name, value in kwargs.items():
            setattr(m, name, value)

        # db.session.commit()
        m.save()

    @classmethod
    def all(cls, **kwargs):
        ms = cls.query.filter_by(**kwargs).all()
        return ms

    @classmethod
    def one(cls, **kwargs):
        ms = cls.query.filter_by(**kwargs).first()
        return ms

    @classmethod
    def columns(cls):
        return cls.__mapper__.c.items()

    def json(self):
        d = dict()
        for attr, column in self.columns():
            if hasattr(self, attr):
                v = getattr(self, attr)
                d[attr] = v
        return d

    def __repr__(self):
        name = self.__class__.__name__
        s = ''
        for attr, column in self.columns():
            if hasattr(self, attr):
                v = getattr(self, attr)
                s += '{}: ({})\n'.format(attr, v)
        return '< {}\n{} >\n'.format(name, s)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def paginate(cls, page, size, **kwargs):
        query = cls.query.filter_by(**kwargs)
        total = query.count()
        items = query.order_by(cls.created_time.desc()).offset((page - 1) * size).limit(size).all()
        return total, items

 
