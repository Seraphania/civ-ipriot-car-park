import sys
sys.path.append("src")

from carpark import Carpark
from display import Display


c = Carpark("Moondalup", 42)
print(c)

d = Display("1", "Welcome to the carpark.")
print(d)