import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from math_blocks.variables import variable
from math_blocks.exponentials import exponential
from math_blocks.fractions import fraction
from math_blocks.complex_numbers import complex_number

class basic_variable(unittest.TestCase):
    def test_basic_latex(self):
        n = variable("x")
        self.assertEqual(n.latex(), "x")

        n2 = variable("y", sign=False)
        self.assertEqual(n2.latex(), "-y")


    def test_basic_eval(self):
        n = variable("x")
        n.value = 5
        self.assertEqual(n.evaluate(), 5)

        n2 = variable("y", sign=False)
        n2.value = 3
        self.assertEqual(n2.evaluate(), -3)

        n3 = variable("z", sign=False)
        # no value set -> error
        self.assertRaises(ValueError, n3.evaluate)

    def test_exponential_eval(self):
        n = variable("x")
        n.value = exponential(2,3)
        self.assertEqual(n.evaluate(), 2**3)

        n2 = variable("y", sign=False)
        n2.value = exponential(2,3, sign=False)
        self.assertEqual(n2.evaluate(), 2**3)

    def test_fraction_eval(self):
        n = variable("x")
        n.value = fraction(2,3)
        self.assertEqual(n.evaluate(), 2/3)

        n2 = variable("y", sign=False)
        n2.value = fraction(2,3, sign=False)
        self.assertEqual(n2.evaluate(), 2/3)

    def test_complex_eval(self):
        n = variable("x")
        n.value = complex_number(2,3)
        self.assertEqual(n.evaluate(), 2+3j)

        n2 = variable("y", sign=False)
        n2.value = complex_number(2,3, sign=False)
        self.assertEqual(n2.evaluate(), 2+3j)


if __name__ == '__main__':
    unittest.main()
