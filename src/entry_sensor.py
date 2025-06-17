from sensor import Sensor

class EntrySensor(Sensor):

    def update_car_park(self, plate):
        self.carpark.add_car(plate)