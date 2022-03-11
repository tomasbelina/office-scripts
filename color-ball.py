from rpi_ws281x import Color
from color import strip, LED_COUNT, LED_MIDDLE, LED_START
import time

ball_color = (0, 0, 255)
previous_color = None

strip.begin()
for pixel_index in range(LED_START, LED_COUNT):
    if previous_color:
        strip.setPixelColor(pixel_index - 1, previous_color)
    previous_color = strip.getPixelColor(pixel_index)
    strip.setPixelColor(pixel_index, Color(*ball_color))
    strip.show()
    time.sleep(0.5)

if previous_color:
    strip.setPixelColor(LED_COUNT - 1, previous_color)
