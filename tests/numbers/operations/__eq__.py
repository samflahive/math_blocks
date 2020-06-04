import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../../..'))
import math_blocks


class number_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_n = math_blocks.number(3)
        n = math_blocks.number(3)
        self.assertEqual(True, main_n == n)
        self.assertEqual(False, main_n == -n)

    def test_variable_eq(self):
        main_n = math_blocks.number(3)
        v = math_blocks.variable("v")
        self.assertEqual(False, main_n == v)

    def test_product_eq(self):
        main_n = math_blocks.number(3)
        p = math_blocks.product([1,2,3])
        self.assertEqual(False, main_n == p)

    def test_poly_eq(self):
        main_n = math_blocks.number(3)
        a = math_blocks.variable("a")
        p = math_blocks.simple_poly([1,2,3], a)
        self.assertEqual(False, main_n == p)

    def test_chain_eq(self):
        main_n = math_blocks.number(3)
        c = math_blocks.chain([1,3,2])

        self.assertEqual(False, main_n == c)

    def test_complex_eq(self):
        main_n = math_blocks.number(3)
        alt_cx_1 = math_blocks.complex_number(1,2)

        self.assertEqual(False, main_n == alt_cx_1)

    def test_exponential_eq(self):
        main_n = math_blocks.number(3)
        e = math_blocks.exponential(1,2)

        self.assertEqual(False, main_n == e)


    def test_exp_eq(self):
        main_n = math_blocks.number(3)
        alt_fr = math_blocks.logarithm(1,2, sign=False)

        self.assertEqual(False, main_n == alt_fr)
        
if __name__ == '__main__':
    unittest.main()
