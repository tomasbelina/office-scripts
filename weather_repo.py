from api import engine
import sqlalchemy
from weather import Weather

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()


def addWeather(humidity, pressure, cpu_temp, indoor_temp, outdoor_temp):
    newWeather = Weather(humidity=humidity, pressure=pressure,
                         cpuTemp=cpu_temp, indoorTemp=indoor_temp, outdoorTemp=outdoor_temp)
    session.add(newWeather)
    session.commit()
