class Sensor:
    def __init__(self,
                 sensor_id: str,
                 active: bool):
        self.sensor_id = sensor_id
        self.active = True

    def car_entry(self):
        pass # update carpark when entry sensor is triggered

    def car_exit(self):
        pass # update carpark when exit sensor is triggered
    
    def update_staus(self):
        pass # Update display information