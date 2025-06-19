from display import Display

class Carpark:
    displays: list[Display]
    def __init__(self,
                 location: str,
                 capacity: int,
                 message: str | None = None,
                 _plates = None,
                 _displays = None): # add data for aggregation

        self.location = location
        self.capacity = capacity
        self.message = message or f"Welcome to {self.location} carpark"
        self.plates = _plates or []
        self.displays = _displays or []

    def __str__(self):
        return f"{self.location} carpark has a capacity of {self.capacity} bays."
    
    @property
    def available_bays(self) -> int:
        available = self.capacity - len(self.plates)
        return max(available, 0)
    
    def register(self, display):
        if not isinstance(display, Display):
            raise TypeError("Component is not a display")
        self.displays.append(display)
        
    def add_car(self, plate: str):
        if plate in self.plates:
            raise ValueError("Vehicle is already in the carpark")
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate: str):
        if plate not in self.plates:
            raise ValueError("This vehicle has not been registered in the carpark")
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        for display in self.displays:
            display.print_to_display({
            "Available Bays": self.available_bays,
            "Current Temperature": 25, # TODO Create module to get current weather from sensor, or maybe an API?
            "Current Time": l, # TODO Update this from sensor
            "Message": self.message,
            })


