import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from unittest.mock import patch
import unittest
from display import Display
from carpark import Carpark # don't think I need this

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(display_id=1,
                               message="Welcome to the carpark",
                               is_active=True)
        
    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.display_id, 1)
        self.assertEqual(self.display.message, "Welcome to the carpark")
        self.assertEqual(self.display.is_active, True)

    def test_print_to_display_default_message_when_data_is_none(self):
        # should print display.message if nothing is passed
        display = Display(display_id=1, message="test no input display message")
        with patch("sys.stdout.write") as mock_write, patch("time.sleep"):
            display.print_to_display(delay=0)
            output = ""

        self.display.print_to_display({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")

        # should print a dictionary passed to it, 