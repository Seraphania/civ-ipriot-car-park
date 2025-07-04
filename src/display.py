from time import sleep
from sys import stdout

class Display:
    def __init__(self,
                 display_id: str,
                 is_active: bool = False,
                 message: str = "Welcome to the Carpark"):

        self.display_id = display_id
        self.is_active = is_active
        self.message = message
        self.display_data = {"Message": self.message}

    def __str__(self) -> str:
        return f"Display {self.display_id}: {self.message}"

    def print_to_display(self, scroll: bool=True, delay: float=0.1, width: int=30):
        """
        Print display information with a scrolling type effect
        Type effect can be disabled for easier debugging with scroll=False
        """
        if scroll == True:
            for key, value in self.display_data.items():            
                line = f"{' ' * width}{key}: {value}{' ' * width}"
                for i in range(len(line) - width + 1):
                    stdout.write(f"|\r|{line[i:i+width]}")
                    stdout.flush()
                    sleep(delay)
        else: # print instantly for quicker debugging
            for key, value in self.display_data.items():
                print(f"{key}: {value}")