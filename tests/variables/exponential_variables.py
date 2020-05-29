import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.variables import variable
from math_blocks.exponentials import exponential

class exponential_variable_test(unittest.TestCase):
    def test_exponential_eval(self):
        n = variable("x")
        n.value = exponential(2,3)
        self.assertEqual(n.evaluate(), 2**3)

        n2 = variable("y", sign=False)
        n2.value = exponential(2,3, sign=False)
        self.assertEqual(n2.evaluate(), 2**3)
