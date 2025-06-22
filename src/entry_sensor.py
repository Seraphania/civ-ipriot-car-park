from sensor import Sensor

class EntrySensor(Sensor):

    def update_car_park(self, plate, temperature):
        self.carpark.temperature = temperature
        self.carpark.add_car(plate)
        