import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from math_blocks.fractions import fraction
from math_blocks.variables import variable

class basic_fraction(unittest.TestCase):
    def test_basic_latex(self):
        # test the latex expression for fractions with numbers only
        fr = fraction(3,2)
        self.assertEqual(fr.latex(), "\\frac{3}{2}")
        fr2 = fraction(-2,2, sign=False)
        self.assertEqual(fr2.latex(), "-\\frac{-2}{2}")

    def test_basic_eval(self):
        fr = fraction(3,2)
        self.assertEqual(fr.evaluate(), 1.5)
        fr2 = fraction(-2,2, sign=False)
        self.assertEqual(fr2.evaluate(), 1)

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
