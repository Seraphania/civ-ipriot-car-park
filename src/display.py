import carpark

class Display:
    def __init__(self,
                 display_id: str,
                 message: str = "",
                 is_on: bool = False):
        self.display_id = display_id
        self.message = message
        self.is_on = is_on

    def __str__(self) -> str:
        return f"Display {self.display_id}: {self.message}"
    

    def update_data(self):
        pass # update information in the data dictionary # TODO: decide if this should be elsewhere

    def display_data(self):
        pass # Print the display data in a nice way