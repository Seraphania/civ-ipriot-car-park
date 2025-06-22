from sensor import Sensor

class EntrySensor(Sensor):

    def update_car_park(self, plate, temperature):
        """
        Add car to list of carpark's plates, and provide an update on the current temperature
        """
        self.carpark.temperature = temperature
        self.carpark.add_car(plate)
        