from time import sleep
from sys import stdout

class Display:
    def __init__(self,
                 display_id: str,
                 message: str = "",
                 is_active: bool = False):
        self.display_id = display_id
        self.message = message
        self.is_on = is_active

    def __str__(self) -> str:
        return f"Display {self.display_id}: {self.message}"

    def update(self, data: dict, delay: float = 0.1, width: int = 40):
        for key, value in data.items():
            line = f"{' ' * width}{key}: {value}{' ' * width}"
            for i in range(len(line) - width + 1):
                stdout.write(f"|\r|{line[i:i+width]}")
                stdout.flush()
                sleep(delay)