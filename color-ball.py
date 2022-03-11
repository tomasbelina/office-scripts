import threading
from color import OfficeStrip
import time
strip =  OfficeStrip()
strip.set_desk_colors()

ball1 = threading.Thread(target=strip.send_ball, args=[(0, 0, 255)])
ball2 = threading.Thread(target=strip.send_ball, args=[(255, 0, 0)])

ball1.start()
time.sleep(1)
ball2.start()

ball1.join()
ball2.join()