import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import unittest
from display import Display

class TestDisplay(unittest.TestCase):
    def SetUp(self):
        self.display = Display(display_id=123,
                               message="Welcome",
                               is_active=True)
        