from display import Display
from datetime import datetime

class Carpark:
    displays: list[Display]
    def __init__(self,
                 location: str,
                 capacity: int,
                 _plates = None,
                 _displays = None):

        self.location = location
        self.capacity = capacity
        self.plates = _plates or []
        self.displays = _displays or []

        self.message = f"Welcome to {self.location} carpark"
        self.temperature = ""

    @property # calculate available bays
    def available_bays(self) -> int:
        available = self.capacity - len(self.plates)
        return max(available, 0)
    
    @property
    def time(self): # retrieve and format current time
        raw_time = datetime.now()
        time = raw_time.strftime("%I:%M %p")
        return time

    def __str__(self):
        return f"{self.location} carpark has a capacity of {self.capacity} bays."
    
    def register(self, display):
        """
        Register new displays and add them to the displays list
        """
        if not isinstance(display, Display):
            raise TypeError("Component is not a display")
        self.displays.append(display)
        
    def add_car(self, plate: str):
        """
        Add plates to the list of plates in the carpark and trigger an update to displays
        """
        if plate in self.plates:
            raise ValueError("Vehicle is already in the carpark")
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate: str):
        """
        Remove plates from the list of plates in the carpark and trigger an update to displays
        """
        if plate not in self.plates:
            raise ValueError("This vehicle has not been registered in the carpark")
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self, scroll_print=True):
        """
        Aggregate display information and trigger display printout
        """
        for display in self.displays:
            display.display_data = {
            "Available Bays": self.available_bays,
            "Current Temperature": self.temperature,
            "Current Time": self.time,
            "Message": self.message,
            }
            display.print_to_display(scroll=scroll_print)