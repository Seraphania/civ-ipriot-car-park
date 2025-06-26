from display import Display
from datetime import datetime
from pathlib import Path
import json

class Carpark:
    displays: list[Display]
    
    def __init__(self,
                 location: str,
                 capacity: int,
                 _plates = None,
                 _displays = None,
                 log_file = None,
                 config_file = None):

        self.location = location
        self.capacity = capacity
        self.plates = _plates or []
        self.displays = _displays or []
        self.log_file = self._init_file(log_file or "log/log.txt")
        self.config_file = self._init_file(config_file or "config.json")
        
        self.message = f"Welcome to {self.location} carpark"
        self.temperature = ""

    @property # calculate available bays
    def available_bays(self) -> int:
        available = self.capacity - len(self.plates)
        return max(available, 0)
    
    @property # retrieve and format current time
    def time(self):
        raw_time = datetime.now()
        time = raw_time.strftime("%I:%M %p")
        return time
    
    @property # retrieve and format current time
    def date(self) -> str:
        raw_time = datetime.now()
        date = f"{raw_time.day}/{raw_time.month}/{raw_time.year}"
        return date

    @classmethod
    def from_config(cls, config_file):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open()as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"], config_file=config["config_file"])

    def write_config(self):
        """
        Store carpark configuration
        """
        with open(self.config_file, "w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": self.log_file,
                       "config_file": self.config_file}, f)

    def _init_file(self, file):
        """
        Create path and file name if not already present
        Return file name
        """
        file_path = Path(file)
        file_path.parent.mkdir(parents=True, exist_ok=True) 
        file_path.touch(exist_ok=True)
        return file
        
    
    def register(self, display):
        """
        Register new displays and add them to the displays list
        """
        if not isinstance(display, Display):
            raise TypeError("Component is not a display")
        self.displays.append(display)
    
    def _log_car(self, plate:str, entry=True):
        """
        Update the log file with car activity
        """
        with Path(self.log_file).open(mode='a', encoding="utf8") as file:
            file.write(f"Car {plate} {'entered' if entry else 'exited'} at {self.time} {self.date}\n")

    def add_car(self, plate: str):
        """
        Add plates to the list of plates in the carpark and trigger an update to displays
        """
        if plate in self.plates:
            raise ValueError("Vehicle is already in the carpark")
        self.plates.append(plate)
        self._log_car(plate)
        self.update_displays()

    def remove_car(self, plate: str):
        """
        Remove plates from the list of plates in the carpark and trigger an update to displays
        """
        if plate not in self.plates:
            raise ValueError("This vehicle has not been registered in the carpark")
        self.plates.remove(plate)
        self._log_car(plate, entry=False)
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
        
    def __str__(self):
        return f"{self.location} carpark has a capacity of {self.capacity} bays."