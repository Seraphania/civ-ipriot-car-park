from abc import ABC, abstractmethod
from random import randint
from carpark import Carpark
from datetime import datetime

class Sensor(ABC):
    def __init__(self,
                 sensor_id: str,
                 carpark: Carpark,
                 is_active: bool = False):
        self.sensor_id = sensor_id
        self.is_active = is_active
        self.carpark = carpark

    @property
    def date(self) -> str:
        raw_time = datetime.now()
        date = f"{raw_time.day}/{raw_time.month}/{raw_time.year}"
        return date
    
    @property
    def time(self):
        raw_time = datetime.now()
        time = raw_time.strftime("%I:%M %p")
        return time
    
    def __str__(self):
        return f"Sensor ID: {self.sensor_id}, Status: {self.is_active}"

    @abstractmethod
    def update_car_park(self, plate: str):
        ...

    def _scan_plate(self):
        return f"FAKE-{randint(0, 9999): 04d}"
    
    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)
