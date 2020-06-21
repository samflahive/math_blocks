import unittest
from math_blocks.algebra.polynomials import Variable, SimplePoly

class num_simple_poly(unittest.TestCase):
    def test_basic_latex(self):
        x = Variable("x")
        p = SimplePoly(coeffs=[1,-2,1], var=x)
        self.assertEqual(p.equiv_num(), False)





if __name__ == '__main__':
    unittest.main()

