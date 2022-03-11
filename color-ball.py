from rpi_ws281x import Color
from color import OfficeStrip, LED_COUNT, LED_MIDDLE, LED_START
import time

strip_color = (255, 0, 0)
ball_color = (0, 0, 255)
previous_color = None

strip =  OfficeStrip()
strip.set_desk_colors()
strip.send_ball()