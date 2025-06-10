class Carpark:
    def __init__(self,
                 location: str,
                 capacity: int,
                 plates: list[str],
                 displays : None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays

    def __str__(self):
        pass # Return a string with the carpark's location and capacity

    def add_car(self):
        pass # Add a car to the carpark

    def remove_car(self):
        pass # Remove a car from the carpark
    
    def update_staus(self):
        pass # Update display information including available bays