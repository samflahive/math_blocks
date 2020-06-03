import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))

from math_blocks.fractions import fraction
from math_blocks.complex_numbers import complex_number

class complex_number_fraction_test(unittest.TestCase):
    def test_fraction_latex(self):

        cp = complex_number(3,2)
        fr = fraction(cp,2)
        
        self.assertEqual(fr.latex(), "\\frac{3+2i}{2}")
        fr3 = - fraction(cp, -complex_number(2,-2))
        self.assertEqual(fr3.latex(), "-\\frac{3+2i}{-(2-2i)}")

    def test_fraction_eval(self):
        cp = complex_number(3,2)
        fr = fraction(cp,2)
        
        self.assertEqual(fr.evaluate(), (3+2j)/2)
        fr3 = - fraction(cp, -complex_number(2,-2))
        self.assertEqual(fr3.evaluate(), -(3+2j)/(-(2-2j)))


if __name__ == '__main__':
    unittest.main()
