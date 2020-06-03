import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../../..'))
import math_blocks


class fraction_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_fr = math_blocks.fraction(1,2)
        n = math_blocks.number(3)
        self.assertEqual(False, main_fr == n)

    def test_variable_eq(self):
        main_fr = math_blocks.fraction(1,2)
        v = math_blocks.variable("v")
        self.assertEqual(False, main_fr == v)

    def test_product_eq(self):
        main_fr = math_blocks.fraction(1,2)
        p = math_blocks.product([1,2,3])
        self.assertEqual(False, main_fr == p)

    def test_poly_eq(self):
        main_fr = math_blocks.fraction(1,2)
        a = math_blocks.variable("a")
        p = math_blocks.simple_poly([1,2,3], a)
        self.assertEqual(False, main_fr == p)

    def test_chain_eq(self):
        main_fr = math_blocks.fraction(1,2)
        c = math_blocks.chain([1,3,2])

        self.assertEqual(False, main_fr == c)

    def test_complex_eq(self):
        main_fr = math_blocks.fraction(1,2)
        alt_cx_1 = math_blocks.complex_number(1,2)

        self.assertEqual(False, main_fr == alt_cx_1)

    def test_fraction_eq(self):
        main_fr = math_blocks.fraction(1,2)
        alt_fr = math_blocks.fraction(1,2, sign=False)

        self.assertEqual(False, main_fr == alt_fr)
        self.assertEqual(True, main_fr == -alt_fr)
        
if __name__ == '__main__':
    unittest.main()
