from rpi_ws281x import PixelStrip, Color
from api import engine
import sqlalchemy
from settings import Settings
import sys
import time

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

settingsJiri = session.query(Settings).filter(
    Settings.type == "COLOR_JIRI").one()
settingsBelca = session.query(Settings).filter(
    Settings.type == "COLOR_BELCA").one()

print(settingsJiri.type)
print(settingsJiri.value)
colorJiri = settingsJiri.value.lstrip("#")
colorRGBJiri = tuple(int(colorJiri[i:i+2], 16) for i in (0, 2, 4))
print('RGB =', colorRGBJiri)

print(settingsBelca.type)
print(settingsBelca.value)
colorBelca = settingsBelca.value.lstrip("#")
colorRGBBelca = tuple(int(colorBelca[i:i+2], 16) for i in (0, 2, 4))
print('RGB =', colorRGBJiri)

LED_COUNT = 150        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
                   LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

for i in range(strip.numPixels()):
    strip.setPixelColor(i, Color(colorJiri[0],colorJiri[1],colorJiri[2]))
    strip.show()
    time.sleep(50 / 1000.0)
