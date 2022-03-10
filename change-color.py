from api import engine
import sqlalchemy
from settings import Settings
import sys

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
type = "COLOR_JIRI"
if(len(sys.argv) == 2 and sys.argv[1] == "Belca"):
    type = "COLOR_BELCA"

settings = session.query(Settings).filter(
    Settings.type == type).one()

print(settings.type)
print(settings.value)
color = settings.value.lstrip("#")
colorRGB = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
print('RGB =', colorRGB )
