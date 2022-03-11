from rpi_ws281x import PixelStrip, Color
from api import get_session
from settings import Settings
import time

LED_START = 0
LED_MIDDLE = 87
LED_COUNT = 150        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

class OfficeStrip:

    def __init__(self):
        self._strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
                                    LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self._strip.begin()

    def set_desk_colors(self):
        session = get_session()
        settingsJiri = session.query(Settings).filter(
            Settings.type == "COLOR_JIRI").one()
        settingsBelca = session.query(Settings).filter(
            Settings.type == "COLOR_BELCA").one()
        colorJiri = settingsJiri.value.lstrip("#")
        colorRGBJiri = tuple(int(colorJiri[i:i+2], 16) for i in (0, 2, 4))
        colorBelca = settingsBelca.value.lstrip("#")
        colorRGBBelca = tuple(
            int(colorBelca[i:i+2], 16) for i in (0, 2, 4))

        for i in range(LED_START, LED_MIDDLE):
            self._strip.setPixelColor(
                i, Color(*colorRGBJiri))

        for i in range(LED_MIDDLE, LED_COUNT):
            self._strip.setPixelColor(
                i, Color(*colorRGBBelca))
        self._strip.show()

    def send_ball(self, ball_color=(0, 0, 255)):
        previous_color = None
        for pixel_index in range(LED_START, LED_COUNT):
            if previous_color:
                self._strip.setPixelColor(pixel_index - 1, previous_color)
            previous_color = self._strip.getPixelColor(pixel_index)
            self._strip.setPixelColor(pixel_index, Color(*ball_color))
            self._strip.show()
            time.sleep(0.1)

        if previous_color:
            self._strip.setPixelColor(LED_COUNT - 1, previous_color)
