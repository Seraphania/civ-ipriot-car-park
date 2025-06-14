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
    
    def register(self, display):
        if not isinstance(display, Display):
            raise TypeError("Component is not a display")
        self._displays.append(display)
        
    def add_car(self):
        ...

    def remove_car(self):
        ...

    def update_displays(self):
        ...
