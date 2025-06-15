from display import Display

class Carpark:
    def __init__(self,
                 location: str,
                 capacity: int,
                 _plates = None,
                 _displays = None):

        self.location = location
        self.capacity = capacity
        self._plates = _plates or []
        self._displays = _displays or []

    def __str__(self):
        return f"{self.location} carpark has a capacity of {self.capacity} bays."
    
    @property
    def available_bays(self) -> int:
        available = self.capacity - len(self._plates)
        return max(available, 0)
    
    def register(self, display):
        if not isinstance(display, Display):
            raise TypeError("Component is not a display")
        self._displays.append(display)
        
    def add_car(self, plate: str):
        if plate in self._plates:
            raise ValueError("Vehicle is already in the carpark")
        self._plates.append(plate)
        self.update_displays()

    def remove_car(self, plate: str):
        if plate not in self._plates:
            raise ValueError("This vehicle has not been registered in the carpark")
        self._plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        data = {
            "Available Bays": self.available_bays,
            "Current Temperature": 25, # TODO Create module to get current weather from an API - Maybe
            "Current Time": "12:00pm", # TODO Update this from sensor
            "Message": f"Welcome to {self.location} Carpark",           
            }
        for display in self._displays:
            display.update(data)

