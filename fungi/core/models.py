# -*- coding: utf-8 -*-
from pathlib import Path

from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, String, JSON, Index
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import NoResultFound

DB_PATH = Path("~/.fungi/cache").expanduser()

Base = declarative_base()
Engine = create_engine(f"sqlite+pysqlite:///{DB_PATH}", future=True)
Session = sessionmaker(Engine)

def initialize():
    with Engine.connect():
        Base.metadata.create_all(Engine)

def dbcache(cls):
    def _cache(f):
        def __cache(session, *a, **kw):
            return [cls.load(session, x) for x in f(*a, **kw)]
        return __cache
    return _cache

class Asset(Base):
    __tablename__ = 'asset'
    __table_args__ = (Index('uniqueness', "opensea_id", "opensea_token_id"), )

    id = Column(Integer, primary_key=True)
    opensea_id = Column(String)
    opensea_token_id = Column(String)
    name = Column(String)
    rank = Column(Integer, nullable=True)
    details = Column(JSON)  # type: ignore

    @classmethod
    def load(cls, session, details):
        stmt = select(cls).filter_by(
            opensea_id       = details["id"],
            opensea_token_id = details["token_id"]
        )
        try:
            result = session.execute(stmt).scalars().one()
        except NoResultFound:
            result = cls(
                opensea_id       = details["id"],
                opensea_token_id = details["token_id"]
            )
            session.add(result)
        result.name = details["name"]
        result.details = details
        return result
