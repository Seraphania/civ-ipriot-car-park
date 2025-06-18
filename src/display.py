from time import sleep
from sys import stdout

class Display:
    def __init__(self,
                 display_id: int,
                 is_active: bool = False,
                 message: str = "Welcome to the Carpark"):

        self.display_id = display_id
        self.message = message
        self.is_active = is_active

    def __str__(self) -> str:
        return f"Display {self.display_id}: {self.message}"

    def print_to_display(self, data: dict | None = None, delay: float = 0.1, width: int = 40):
        if data is None:
            data = {"Message": self.message}
        for key, value in data.items():
            line = f"{' ' * width}{key}: {value}{' ' * width}"
            for i in range(len(line) - width + 1):
                stdout.write(f"|\r|{line[i:i+width]}")
                stdout.flush()
                sleep(delay)

            