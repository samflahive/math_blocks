import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))

from math_blocks.fractions import fraction
from math_blocks.variables import variable

class variable_fraction_test(unittest.TestCase):
    def test_variable_latex(self):
        x = variable("x", value=2, sign=True)
        fr = fraction(3,x)
        self.assertEqual(fr.latex(), "\\frac{3}{x}")

        y = variable("y", value=2, sign=False)
        fr2 = fraction(x,y, sign=False)
        fr3 = -fr2
        self.assertEqual(fr3.latex(), "\\frac{x}{-y}")

    def test_variable_eval(self):
        x = variable("x", value=2, sign=True)
        fr = fraction(3,x)
        self.assertEqual(fr.evaluate(), 1.5)

        y = variable("y", value=2, sign=False)
        fr2 = fraction(x,y, sign=False)
        fr3 = -fr2
        self.assertEqual(fr3.evaluate(), -1)


if __name__ == '__main__':
    unittest.main()
