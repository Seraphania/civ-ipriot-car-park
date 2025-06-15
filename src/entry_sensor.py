from sensor import Sensor

# from carpark import Carpark

class EntrySensor(Sensor):

    def update_car_park(self, plate):
        self.carpark.add_car(plate)