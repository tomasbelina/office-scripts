from api import engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Weather(Base):
    __tablename__ = 'Weather'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    humidity = sqlalchemy.Column(sqlalchemy.Numeric(6.2), nullable=False)
    pressure = sqlalchemy.Column(sqlalchemy.Numeric(6.2), nullable=False)
    cpuTemp = sqlalchemy.Column(sqlalchemy.Numeric(6.2), nullable=False)
    indoorTemp = sqlalchemy.Column(sqlalchemy.Numeric(6.2), nullable=False)
    outdoorTemp = sqlalchemy.Column(sqlalchemy.Numeric(6.2), nullable=False)
    created = sqlalchemy.Column(sqlalchemy.DateTime)


Base.metadata.create_all(engine)
