from abc import ABC, abstractmethod
from random import randint
from carpark import Carpark


class Sensor(ABC):
    def __init__(self,
                 sensor_id: str,
                 carpark: Carpark,
                 is_active: bool = False):
        self.sensor_id = sensor_id
        self.is_active = is_active
        self.carpark = carpark
    
    def __str__(self):
        return f"Sensor ID: {self.sensor_id}, Status: {self.is_active}"

    @abstractmethod
    def update_carpark(self, plate: str, temperature:str):
        ...

    def _scan_plate(self): # hacky for the sake of simulation
        return f"FAKE-{randint(0, 9999):04d}"
    
    def _scan_temperature(self):
        """
        Returns the current temperature from the sensors (imaginary) thermometer
        """
        temp = randint(8, 46)  # hacky for the sake of simulation
        return f"{temp} \u00b0C"
    
    def detect_vehicle(self):
        plate = self._scan_plate()
        temperature = self._scan_temperature()
        self.update_carpark(plate, temperature)
