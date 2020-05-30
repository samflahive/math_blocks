import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.numbers import number
from math_blocks.variables import variable
from math_blocks.simple_polys import simple_poly

class basic_simple_poly(unittest.TestCase):
    def test_basic_latex(self):
        x = variable("x")
        p = simple_poly(coeffs=[1,-2,1], var=x)
        self.assertEqual(p.latex(), "1x^{2}-2x+1")

    def test_basic_eval(self):
        x = variable("x")
        p = simple_poly(coeffs=[1,-2,1], var=x)
        x.value = 2
        self.assertEqual(p.evaluate(), 1)




if __name__ == '__main__':
    unittest.main()
