from sensor import Sensor
from random import choice

class ExitSensor(Sensor):

    def update_car_park(self, plate):
        self.carpark.remove_car(plate)

    def _scan_plate(self):
        return choice(self.carpark._plates)