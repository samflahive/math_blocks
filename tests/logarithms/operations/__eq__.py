import unittest

import math_blocks


class logarithm_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_lg = math_blocks.logarithm(1,2)
        n = math_blocks.number(3)
        self.assertEqual(False, main_lg == n)

    def test_variable_eq(self):
        main_lg = math_blocks.logarithm(1,2)
        v = math_blocks.variable("v")
        self.assertEqual(False, main_lg == v)

    def test_product_eq(self):
        main_lg = math_blocks.logarithm(1,2)
        p = math_blocks.product([1,2,3])
        self.assertEqual(False, main_lg == p)

    def test_poly_eq(self):
        main_lg = math_blocks.logarithm(1,2)
        a = math_blocks.variable("a")
        p = math_blocks.simple_poly([1,2,3], a)
        self.assertEqual(False, main_lg == p)

    def test_chain_eq(self):
        main_lg = math_blocks.logarithm(1,2)
        c = math_blocks.chain([1,3,2])

        self.assertEqual(False, main_lg == c)

    def test_complex_eq(self):
        main_lg = math_blocks.logarithm(1,2)
        alt_cx_1 = math_blocks.complex_number(1,2)

        self.assertEqual(False, main_lg == alt_cx_1)

    def test_exponential_eq(self):
        main_lg = math_blocks.logarithm(1,2)
        e = math_blocks.exponential(1,2)

        self.assertEqual(False, main_lg == e)


    def test_exp_eq(self):
        main_lg = math_blocks.logarithm(1,2)
        alt_fr = math_blocks.logarithm(1,2, sign=False)

        self.assertEqual(False, main_lg == alt_fr)
        self.assertEqual(True, main_lg == -alt_fr)
        
if __name__ == '__main__':
    unittest.main()
