import sys
sys.path.append("src")

from carpark import Carpark
from display import Display
from entry_sensor import EntrySensor
from exit_sensor import ExitSensor


carpark = Carpark(location="Moondalup", capacity=100, log_file="moondalup.txt", config_file="moondalup_config.json")
carpark.write_config()
carpark = Carpark.from_config(config_file="moondalup_config.json")
entry_sensor = EntrySensor(sensor_id="1", carpark=carpark, is_active=True)
exit_sensor = ExitSensor(sensor_id="2", carpark=carpark, is_active=True)
carpark.register(Display(display_id="1", is_active=True, message="Welcome to Moondalup"))
for i in range(10):
    entry_sensor.detect_vehicle()

for i in range(2):
    exit_sensor.detect_vehicle()