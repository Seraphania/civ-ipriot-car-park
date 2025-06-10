class Carpark:
    def __init__(self,
                 location: str,
                 capacity: int):

        self.location = location
        self.capacity = capacity
        self._plates = None or []
        self._displays = ''

    def __str__(self):
        carpark_info = f"{self.location} carpark has a capacity of {self.capacity} bays."
        return carpark_info

    def add_car(self):
        pass # Add a car to the carpark

    def remove_car(self):
        pass # Remove a car from the carpark
    
    def update_staus(self):
        pass # Update display information including available bays