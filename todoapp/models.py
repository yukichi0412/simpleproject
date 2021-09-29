from django.db import models
from sqlalchemy import Column, Integer, String, DateTime, Sequence
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from config.db import Base, create_engine, make_session

class DjangoLikeModelMixin(object):
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class Category(Base, DjangoLikeModelMixin):
    __tablename__ = 'categories'

    title = Column(String(20))
    created_at = Column('created', DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return self.title

class Task():
    __tablename__ = 'tasks'

    title = Column(String(20))
    