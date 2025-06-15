import sys
sys.path.append("src")

from carpark import Carpark
from display import Display

c = Carpark("Moondalup", 42)
d = Display("display_1")

c.register(d)

c.update_displays()