import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.variables import variable
from math_blocks.fractions import fraction

class fraction_variable_test(unittest.TestCase):
    def test_fraction_eval(self):
        n = variable("x")
        n.value = fraction(2,3)
        self.assertEqual(n.evaluate(), 2/3)

        n2 = variable("y", sign=False)
        n2.value = fraction(2,3, sign=False)
        self.assertEqual(n2.evaluate(), 2/3)
