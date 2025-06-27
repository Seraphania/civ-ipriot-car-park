from sensor import Sensor
from random import choice

class ExitSensor(Sensor):

    def update_carpark(self, plate, temperature):
        """
        Remove exiting car from list of carpark's plates, and provide an update on the current temperature
        """
        self.carpark.temperature = temperature
        self.carpark.remove_car(plate)


    def _scan_plate(self): # hacky for the sake of simulation
        return choice(self.carpark.plates)