# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Type, Callable, Dict, Any

from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, String, JSON, Index
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import Session as SessionClass
from sqlalchemy.exc import NoResultFound

DB_PATH = Path("~/.fungi/cache").expanduser()

Base = declarative_base()
Engine = create_engine(f"sqlite+pysqlite:///{DB_PATH}", future=True)
Session = sessionmaker(Engine)

def initialize() -> None:
    with Engine.connect():
        Base.metadata.create_all(Engine)

class LoadableMixin:
    @classmethod
    def load(cls: Type[Base], session: SessionClass, details: Dict[Any, Any]) -> Any:  # type: ignore
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
            )  # type: ignore
            session.add(result)
        result.name = details["name"]  # pylint: disable=attribute-defined-outside-init
        result.details = details  # pylint: disable=attribute-defined-outside-init
        return result

def dbcache(cls: Type[LoadableMixin]) -> Callable[[Any], Any]:
    def _cache(f: Callable[[Any], Any]) -> Callable[[Any], Any]:
        def __cache(session, *a, **kw):  # type: ignore
            return [cls.load(session, x) for x in f(*a, **kw)]  # type: ignore
        return __cache
    return _cache

class Asset(Base, LoadableMixin):
    __tablename__ = 'asset'
    __table_args__ = (Index('uniqueness', "opensea_id", "opensea_token_id"), )

    id = Column(Integer, primary_key=True)
    opensea_id = Column(String)
    opensea_token_id = Column(String)
    name = Column(String)
    rank = Column(Integer, nullable=True)
    details = Column(JSON)
