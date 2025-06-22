import sys
sys.path.append("src")

from carpark import Carpark
from display import Display
from entry_sensor import EntrySensor
from exit_sensor import ExitSensor


carpark = Carpark("Moondalup", 42)
entry_sensor = EntrySensor("Entry Sensor", carpark, is_active=True)
exit_sensor = ExitSensor("Exit Sensor", carpark, is_active=True)
carpark.register(Display(1, is_active=True))
entry_sensor.detect_vehicle()