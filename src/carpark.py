# carpark.py
class Carpark:
    def __init__(self,
                 location: str,
                 capacity: int = 42):

        self.location = location
        self.capacity = capacity
        self._plates = None or []
        self._displays = ''

    def __str__(self):
        return f"{self.location} carpark has a capacity of {self.capacity} bays."

    def add_car(self):
        pass # Add a car to the carpark

    def remove_car(self):
        pass # Remove a car from the carpark
    
    def update_status(self):
        pass # Update display information including available bays