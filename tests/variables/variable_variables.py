import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.variables import variable

class variable_variable_test(unittest.TestCase):
    def test_variable_eval(self):
        x = variable("x")
        x.value = variable("y", value=3)
        self.assertEqual(x.evaluate(), 3)

        y = variable("y", value=3, sign=False)
        x.value = y
        self.assertEqual(x.evaluate(), -3)
