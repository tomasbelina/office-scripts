import board
import neopixel
from api import engine
import sqlalchemy
from settings import Settings
import sys

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

settingsJiri = session.query(Settings).filter(
    Settings.type == "COLOR_JIRI").one()
settingsBelca = session.query(Settings).filter(
    Settings.type == "COLOR_BELCA").one()

print(settingsJiri.type)
print(settingsJiri.value)
color = settingsJiri.value.lstrip("#")
colorRGB = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
print('RGB =', colorRGB)

print(settingsBelca.type)
print(settingsBelca.value)
color = settingsBelca.value.lstrip("#")
colorRGB = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
print('RGB =', colorRGB)

pixel_pin = board.D18
num_pixels = 150
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
pixels.fill(colorRGB)
