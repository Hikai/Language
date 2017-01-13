"""
SQLAlchemy base code example.

. . .
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

BASE = declarative_base()


class User(BASE):
    """Table table class."""

    __tablename__ = "users"
    no = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
