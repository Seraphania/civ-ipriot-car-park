import carpark

class Display:
    def __init__(self,
                 display_id: str,
                 data: dict):
        self.display_id = display_id
        self.data = {"Location": '', # TODO: carpark.location implement this
                     "Bays": "",
                     "Message": '',
                     "Temperature": '',
                     }

    def update_data(self):
        pass # update infomration in the data dictionary # TODO: decide if this should be elsewhere

    def display_data(self):
        pass # Print the display data in a nice way