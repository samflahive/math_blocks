import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from math_blocks.fractions import fraction


class basic_fraction(unittest.TestCase):
    def test_basic_latex(self):
        # test the latex expression for fractions with numbers only
        fr = fraction(3,2)
        self.assertEqual(fr.latex(), "\\frac{3}{2}")
        fr2 = fraction(-2,2)
        self.assertEqual(fr2.latex(), "\\frac{-2}{2}")

    def test_basic_eval(self):
        fr = fraction(3,2)
        self.assertEqual(fr.evaluate(), 1.5)
        fr2 = fraction(-2,2)
        self.assertEqual(fr2.evaluate(), -1)




if __name__ == '__main__':
    unittest.main()
