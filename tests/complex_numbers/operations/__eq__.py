import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../../..'))
import math_blocks


class complex_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_cx = math_blocks.complex_number(1,2)
        n = math_blocks.number(3)
        self.assertEqual(False, main_cx == n)

    def test_variable_eq(self):
        main_cx = math_blocks.complex_number(1,2)
        v = math_blocks.variable("v")
        self.assertEqual(False, main_cx == v)

    def test_product_eq(self):
        main_cx = math_blocks.complex_number(1,2)
        p = math_blocks.product([1,2,3])
        self.assertEqual(False, main_cx == p)

    def test_poly_eq(self):
        main_cx = math_blocks.complex_number(1,2)
        a = math_blocks.variable("a")
        p = math_blocks.simple_poly([1,2,3], a)
        self.assertEqual(False, main_cx == p)

    def test_chain_eq(self):
        main_cx = math_blocks.complex_number(1,2)
        c = math_blocks.chain([1,3,2])

        self.assertEqual(False, main_cx == c)

    def test_complex_eq(self):
        main_cx = math_blocks.complex_number(1,2)
        alt_cx_1 = math_blocks.complex_number(1,2)
        alt_cx_2 = math_blocks.complex_number(1,-2)

        self.assertEqual(True, main_cx == alt_cx_1)
        self.assertEqual(False, main_cx == alt_cx_2)

if __name__ == '__main__':
    unittest.main()
