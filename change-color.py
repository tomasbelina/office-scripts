from api import engine
import sqlalchemy
from settings import Settings

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

settingsJiri = session.query(Settings).filter(
    Settings.type == 'COLOR_JIRI').one()
settingsBelca = session.query(Settings).filter(
    Settings.type == 'COLOR_BELCA').one()

print(settingsJiri.value)
print(settingsBelca.value)
