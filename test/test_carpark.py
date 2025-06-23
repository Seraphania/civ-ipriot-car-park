import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve() / "../src"))

import unittest

from carpark import Carpark
from display import Display

log_file = Path("log/test_log.txt")

class TestCarpark(unittest.TestCase):
      def setUp(self):
         self.carpark = Carpark("123 Example Street", 100)

      def test_carpark_initialized_with_all_attributes(self):
         self.assertEqual(self.carpark.log_file, Path("log/log.txt"))
         self.assertIsInstance(self.carpark, Carpark)
         self.assertEqual(self.carpark.location, "123 Example Street")
         self.assertEqual(self.carpark.capacity, 100)
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
         self.carpark.register(Display(1, is_active=True))
         self.carpark.register(Display(2, is_active=True))
         self.carpark.update_displays(scroll_print=False) # Print instantly without scrolling effect for testing
         for display in self.carpark.displays:
            self.assertEqual(display.display_data["Available Bays"], self.carpark.available_bays)
            self.assertEqual(display.display_data["Current Temperature"], self.carpark.temperature)
            self.assertEqual(display.display_data["Current Time"], self.carpark.time)
            self.assertEqual(display.display_data["Message"], self.carpark.message)
            
      def test_log_file_created(self):
         new_carpark = Carpark(location="Moondalup", capacity=100, log_file=log_file)
         self.assertTrue(Path("log/test_log.txt").exists())

      def test_car_logged_when_entering(self):
         new_carpark = Carpark("123 Example Street", 100, log_file=log_file)
         new_carpark.add_car("NEW-001")
         with new_carpark.log_file.open() as f:
               last_line = f.readlines()[-1]
         self.assertIn("NEW-001", last_line) # check plate entered
         self.assertIn("entered", last_line) # check description
         self.assertIn("\n", last_line) # check entry has a new line

      def test_car_logged_when_exiting(self):
         new_carpark = Carpark("123 Example Street", 100, log_file=log_file) 
         new_carpark.add_car("NEW-001")
         new_carpark.remove_car("NEW-001")
         with new_carpark.log_file.open() as f:
               last_line = f.readlines()[-1]
         self.assertIn("NEW-001", last_line)# (last_line, "NEW-001") # check plate entered
         self.assertIn("exited", last_line) # check description
         self.assertIn("\n", last_line) # check entry has a new line

      def tearDown(self):
         Path("log/test_log.txt").unlink(missing_ok=True)
 