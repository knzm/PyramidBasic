# -*- coding: utf-8 -*-

from sqlalchemy import engine_from_config
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension

__all__ = ['DBSession', 'BaseModel', 'setup_model', 'create_all']

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


class BaseModel(declarative_base()):
    __abstract__ = True

    @classmethod
    def query(cls):
        return DBSession.query(cls)


def init(engine):
    DBSession.remove()
    DBSession.configure(bind=engine)


def setup_model(settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    init(engine)
    BaseModel.metadata.bind = engine


def create_all():
    BaseModel.metadata.create_all()
