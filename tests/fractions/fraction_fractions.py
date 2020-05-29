import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))

from math_blocks.fractions import fraction

class fraction_fraction_test(unittest.TestCase):
    def test_fraction_latex(self):

        fr = fraction(3,2)
        fr2 = fraction(fr,-fr)
        
        self.assertEqual(fr2.latex(), "\\frac{\\frac{3}{2}}{-\\frac{3}{2}}")
        fr3 = - fr2
        self.assertEqual(fr3.latex(), "-\\frac{\\frac{3}{2}}{-\\frac{3}{2}}")

    def test_fraction_eval(self):
        fr = fraction(3,2)
        fr2 = fraction(fr,-fr)
        
        self.assertEqual(fr2.evaluate(), (3/2)/(-3/2))
        fr3 = - fr2
        self.assertEqual(fr3.evaluate(), (3/2)/(3/2))

    



if __name__ == '__main__':
    unittest.main()
