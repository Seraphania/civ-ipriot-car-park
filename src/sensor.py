from carpark import Carpark

class Sensor:
    def __init__(self,
                 sensor_id: str,
                 carpark: Carpark,
                 is_active: bool = False):
        self.sensor_id = sensor_id
        self.is_active = is_active
        self.carpark = carpark

    def __str__(self):
        return f"Sensor ID: {self.sensor_id}, Status: {self.is_active}"

class EntrySensor(Sensor):
    ...
    
    def car_entry(self):
        pass # update carpark when entry sensor is triggered

class ExitSensor(Sensor):
    ...

    def car_exit(self):
        pass # update carpark when exit sensor is triggered