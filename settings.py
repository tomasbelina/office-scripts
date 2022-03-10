from api import engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Settings(Base):
    __tablename__ = 'Settings'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    type = sqlalchemy.Column(sqlalchemy.String)
    value = sqlalchemy.Column(sqlalchemy.String)
    updated = sqlalchemy.Column(sqlalchemy.DateTime)
    created = sqlalchemy.Column(sqlalchemy.DateTime)


Base.metadata.create_all(engine)
