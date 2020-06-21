import unittest

from math_blocks.algebra.core import Chain, Number
from math_blocks.algebra.polynomials import SimplePoly, Variable


class polynomial_eq(unittest.TestCase):

    
    def test_number_eq(self):
        x = Variable("x")
        main_poly = SimplePoly([1,2,3], x)
        n = Number(3)
        self.assertEqual(False, main_poly == n)


    def test_poly_eq(self):
        x = Variable("x")
        main_poly = SimplePoly([1,2,3], x)
        a = Variable("a")
        p = SimplePoly([1,2,3], a)

        alt_x =  SimplePoly([1,2,3], x)
        alt_x_2 =  SimplePoly([1,1,3], x)
        
        self.assertEqual(False, main_poly == p)
        self.assertEqual(True, main_poly == alt_x)
        self.assertEqual(False, main_poly == alt_x_2)

    def test_chain_eq(self):
        x = Variable("x")
        main_poly = SimplePoly([1,2,3], x)
        c = Chain([1,3,2])

        self.assertEqual(False, main_poly == c)

        
if __name__ == '__main__':
    unittest.main()
