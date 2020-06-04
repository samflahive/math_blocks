import unittest

import math_blocks


class product_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_p = math_blocks.product([1,2,3])
        n = math_blocks.number(2)
        self.assertEqual(False, main_p == n)

    def test_variable_eq(self):
        main_p = math_blocks.product([1,2,3])
        v = math_blocks.variable("v")
        self.assertEqual(False, main_p == v)

    def test_product_eq(self):
        main_p = math_blocks.product([1,2,3])
        p = math_blocks.product([1,2,3], sign=False)
        p2 = math_blocks.product([2,1,3])
        self.assertEqual(False, main_p == p)
        self.assertEqual(False, main_p == p2)
        self.assertEqual(True, main_p == -p)

    def test_poly_eq(self):
        main_p = math_blocks.product([1,2,3])
        a = math_blocks.variable("a")
        p = math_blocks.simple_poly([1,2,3], a)
        self.assertEqual(False, main_p == p)

    def test_chain_eq(self):
        main_p = math_blocks.product([1,2,3])
        c = math_blocks.chain([1,3,2])

        self.assertEqual(False, main_p == c)

    def test_complex_eq(self):
        main_p = math_blocks.product([1,2,3])
        alt_cx_1 = math_blocks.complex_number(1,2)

        self.assertEqual(False, main_p == alt_cx_1)

    def test_exponential_eq(self):
        main_p = math_blocks.product([1,2,3])
        e = math_blocks.exponential(1,2)

        self.assertEqual(False, main_p == e)


    def test_exp_eq(self):
        main_p = math_blocks.product([1,2,3])
        alt_fr = math_blocks.logarithm(1,2, sign=False)

        self.assertEqual(False, main_p == alt_fr)
        
if __name__ == '__main__':
    unittest.main()
