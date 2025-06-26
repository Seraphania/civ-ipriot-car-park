import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


import unittest
from display import Display

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(display_id="1",
                               is_active=True,
                               message="Test Message",
                               )
        
    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.display_id, "1")
        self.assertEqual(self.display.is_active, True)
        self.assertEqual(self.display.message, "Test Message")
        self.assertEqual(self.display.display_data["Message"], "Test Message")
