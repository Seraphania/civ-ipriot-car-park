# import sys
from pathlib import Path
# sys.path.insert(0, str(Path(__file__).resolve() / "../src"))

import unittest
import json

from carpark import Carpark
from display import Display

log = "log/test_log.txt" # avoid overwriting "official" logs during testing
config = "test_config.json" # avoid overwriting "official" config files during testing

class TestCarpark(unittest.TestCase):
      def setUp(self):
         self.carpark = Carpark(location="123 Example Street", capacity=100, log_file=log, config_file=config)

      def test_carpark_initialized_with_all_attributes(self):
         self.assertIsInstance(self.carpark, Carpark)
         self.assertEqual(self.carpark.location, "123 Example Street")
         self.assertEqual(self.carpark.capacity, 100)
         self.assertEqual(self.carpark.log_file, log)
         self.assertEqual(self.carpark.config_file, config)
         self.assertEqual(self.carpark.plates, [])
         self.assertEqual(self.carpark.displays, [])
         self.assertEqual(self.carpark.message, "Welcome to 123 Example Street carpark")
         self.assertEqual(self.carpark.temperature, "")
         self.assertEqual(self.carpark.available_bays, 100)
         self.assertIsNotNone(self.carpark.time)

      def test_register_raises_type_error(self):
         with self.assertRaises(TypeError):
            self.carpark.register("Not a display")

      def test_add_car(self):
         self.carpark.add_car("FAKE-001")
         self.assertEqual(self.carpark.plates, ["FAKE-001"])
         self.assertEqual(self.carpark.available_bays, 99)

      def test_remove_car(self):
         self.carpark.add_car("FAKE-001")
         self.carpark.remove_car("FAKE-001")
         self.assertEqual(self.carpark.plates, [])
         self.assertEqual(self.carpark.available_bays, 100)

      def test_overfill_the_carpark(self):
         for i in range(100):
            self.carpark.add_car(f"FAKE-{i}")
         self.assertEqual(self.carpark.available_bays, 0)
         self.carpark.add_car("FAKE-100")
         # Overfilling the car park should not change the number of available bays
         self.assertEqual(self.carpark.available_bays, 0)

         # Removing a car from an overfilled car park should not change the number of available bays
         self.carpark.remove_car("FAKE-100")
         self.assertEqual(self.carpark.available_bays, 0)

      def test_removing_a_car_that_does_not_exist(self):
         with self.assertRaises(ValueError):
            self.carpark.remove_car("NO-1")

      def test_update_displays_updates_display_data(self):
         # The display.display_data attribute for each display should be updated with the dictionary content
         self.carpark.temperature = "22°C"
         self.carpark.register(Display("1", is_active=True))
         self.carpark.register(Display("2", is_active=True))
         self.carpark.update_displays(scroll_print=False) # Print instantly without scrolling effect for testing
         for display in self.carpark.displays:
            self.assertEqual(display.display_data["Available Bays"], self.carpark.available_bays)
            self.assertEqual(display.display_data["Current Temperature"], self.carpark.temperature)
            self.assertEqual(display.display_data["Current Time"], self.carpark.time)
            self.assertEqual(display.display_data["Message"], self.carpark.message)
            
      def test_log_file_created(self):
         self.assertTrue(Path(log).exists())

      def test_car_logged_when_entering(self):
         self.carpark.add_car("NEW-001")
         with Path(self.carpark.log_file).open() as f:
               last_line = f.readlines()[-1]
         self.assertIn("NEW-001", last_line) # check plate entered
         self.assertIn("entered", last_line) # check description
         self.assertIn("\n", last_line) # check entry has a new line

      def test_car_logged_when_exiting(self):
         self.carpark.add_car("NEW-001")
         self.carpark.remove_car("NEW-001")
         with Path(self.carpark.log_file).open() as f:
               last_line = f.readlines()[-1]
         self.assertIn("NEW-001", last_line)# (last_line, "NEW-001") # check plate entered
         self.assertIn("exited", last_line) # check description
         self.assertIn("\n", last_line) # check entry has a new line

      def test_write_config_creates_valid_json(self):
         self.carpark.write_config()
         # newly created config should exist on disk 
         self.assertTrue(Path(config).exists()) 
         data = json.loads(Path(config).read_text())

         # config_file location, capacity and log file should match the carpark that wrote the config
         self.assertEqual(data["location"], "123 Example Street") 
         self.assertEqual(data["capacity"], 100)
         self.assertEqual(data["log_file"], log)

      def test_carpark_loads_from_config(self):
         self.carpark.write_config()
         new_carpark = self.carpark.from_config(config_file=config)
         # In a carpark created from config, the location, capacity and log file should match the carpark that wrote the config
         self.assertIsInstance(new_carpark, Carpark)
         self.assertEqual(new_carpark.location, "123 Example Street")
         self.assertEqual(new_carpark.capacity, 100)
         self.assertEqual(new_carpark.log_file, log)

      def tearDown(self): # remove logs and config files used for testing
         Path(log).unlink(missing_ok=True)
         Path(config).unlink(missing_ok=True)
         Path("new_log.txt").unlink(missing_ok=True)