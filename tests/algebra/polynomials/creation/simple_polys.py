import unittest
from math_blocks.algebra.polynomials import Variable, SimplePoly

class basic_simple_poly(unittest.TestCase):
    def test_basic_latex(self):
        x = Variable("x")
        p = SimplePoly(coeffs=[1,-2,1], var=x)
        self.assertEqual(p.latex(), "1x^{2}-2x+1")

    def test_basic_eval(self):
        x = Variable("x")
        p = SimplePoly(coeffs=[1,-2,1], var=x)
        x.value = 2
        self.assertEqual(p.evaluate(), 1)




if __name__ == '__main__':
    unittest.main()
