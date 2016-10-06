"""
SQLite db.

test db
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine, Column, Integer, String

ENGINE = create_engine('sqlite:///db.sqlite', echo=True)
BASE = declarative_base()


class User(BASE):
    """User mapping class."""

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    passwd = Column(String(100), nullable=False)
    attk = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)

    def __init__(self, name, passwd, attk, level):
        """User class init method."""
        self.name = name
        self.passwd = passwd
        self.attk = attk
        self.level = level

    def __repr__(self):
        """User class print method."""
        return "<User({}, {}, {}".format(self.name, self.attk, self.level)

if not database_exists(ENGINE.url):
    create_database(ENGINE.url)

BASE.metadata.create_all(ENGINE)
