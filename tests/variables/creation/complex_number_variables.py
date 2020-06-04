import unittest

from math_blocks.variables import variable
from math_blocks.complex_numbers import complex_number

class complex_number_variable_test(unittest.TestCase):
    def test_complex_eval(self):
        n = variable("x")
        n.value = complex_number(2,3)
        self.assertEqual(n.evaluate(), 2+3j)

        n2 = variable("y", sign=False)
        n2.value = complex_number(2,3, sign=False)
        self.assertEqual(n2.evaluate(), 2+3j)
