import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


import unittest
from entry_sensor import EntrySensor
from exit_sensor import ExitSensor
from carpark import Carpark
from pathlib import Path

log = "log/test_log.txt" # avoid overwriting "official" logs during testing
config = "test_config.json" # avoid overwriting "official" config files during testing

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.carpark = Carpark(location="Testpark", capacity=42, log_file=log, config_file=config)

        self.entry_sensor = EntrySensor(sensor_id="Entry Test", 
                                       carpark=self.carpark,
                                       is_active=True)

        self.exit_sensor = ExitSensor(sensor_id="Exit Test", 
                                       carpark=self.carpark,
                                       is_active=True)

    # Entry Sensor
    def test_entry_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor,EntrySensor)
        self.assertEqual(self.entry_sensor.sensor_id, "Entry Test")
        self.assertEqual(self.entry_sensor.carpark, self.carpark)
        self.assertEqual(self.entry_sensor.is_active, True)

    def test_exit_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.sensor_id, "Exit Test")
        self.assertEqual(self.exit_sensor.carpark, self.carpark)
        self.assertEqual(self.exit_sensor.is_active, True)

    def test_sensor_update_carpark(self):
        # Entry sensor should add a plate and update the carpark temperature
        self.entry_sensor.update_carpark(plate="TEST-001", temperature="30 Degrees")
        self.assertIn("TEST-001", self.carpark.plates)
        self.assertEqual(self.carpark.temperature, "30 Degrees")

        # Exit sensor should remove a plate from plates and update the temperature
        self.exit_sensor.update_carpark(plate="TEST-001", temperature="40 Degrees")
        self.assertNotIn("TEST-001", self.carpark.plates)
        self.assertEqual(self.carpark.temperature, "40 Degrees")
        
    def tearDown(self): # remove logs and config files used for testing
        Path(log).unlink(missing_ok=True)
        Path(config).unlink(missing_ok=True)

    