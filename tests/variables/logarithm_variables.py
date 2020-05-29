import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.variables import variable
from math_blocks.logarithms import logarithm
from math import log

class logarithm_variable_test(unittest.TestCase):
    def test_logarithm_eval(self):
        n = variable("x")
        n.value = logarithm(3,2,sign=False)
        self.assertEqual(n.evaluate(), -log(3,2))

        n2 = variable("y", sign=False)
        n2.value = logarithm(3,2,sign=False)
        self.assertEqual(n2.evaluate(), log(3,2))

        n3 = variable("z", sign=False)
        # no value set -> error
        self.assertRaises(ValueError, n3.evaluate)


