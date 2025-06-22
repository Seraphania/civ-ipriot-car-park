from sensor import Sensor
from random import choice

class ExitSensor(Sensor):

    def update_car_park(self, plate, temperature):
        self.carpark.remove_car(plate)
        self.carpark.temperature = temperature

    def _scan_plate(self): # hacky for the sake of simulation
        return choice(self.carpark.plates)