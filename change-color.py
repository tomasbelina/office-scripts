from rpi_ws281x import PixelStrip, Color
from api import engine
import sqlalchemy
from settings import Settings
import sys
import time

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

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
try:
    while True:
        settingsJiri = session.query(Settings).filter(
            Settings.type == "COLOR_JIRI").one()
        settingsBelca = session.query(Settings).filter(
            Settings.type == "COLOR_BELCA").one()

        colorJiri = settingsJiri.value.lstrip("#")
        colorRGBJiri = tuple(int(colorJiri[i:i+2], 16) for i in (0, 2, 4))
        colorBelca = settingsBelca.value.lstrip("#")
        colorRGBBelca = tuple(int(colorBelca[i:i+2], 16) for i in (0, 2, 4))

        for i in range(0, 87):
            strip.setPixelColor(
                i, Color(colorRGBJiri[0], colorRGBJiri[1], colorRGBJiri[2]))
            strip.show()

        for i in range(87, 150):
            strip.setPixelColor(
                i, Color(colorRGBBelca[0], colorRGBBelca[1], colorRGBBelca[2]))
            strip.show()
except KeyboardInterrupt:
    for i in range(0, 150):
        strip.setPixelColor(
            i, Color(0, 0, 0))
        strip.show()
