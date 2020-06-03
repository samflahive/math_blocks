import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../../..'))
import math_blocks


class polynomial_eq(unittest.TestCase):

    
    def test_number_eq(self):
        x = math_blocks.variable("x")
        main_poly = math_blocks.simple_poly([1,2,3], x)
        n = math_blocks.number(3)
        self.assertEqual(False, main_poly == n)

    def test_variable_eq(self):
        x = math_blocks.variable("x")
        main_poly = math_blocks.simple_poly([1,2,3], x)
        v = math_blocks.variable("v")
        self.assertEqual(False, main_poly == v)

    def test_product_eq(self):
        x = math_blocks.variable("x")
        main_poly = math_blocks.simple_poly([1,2,3], x)
        p = math_blocks.product([1,2,3])
        self.assertEqual(False, main_poly == p)

    def test_poly_eq(self):
        x = math_blocks.variable("x")
        main_poly = math_blocks.simple_poly([1,2,3], x)
        a = math_blocks.variable("a")
        p = math_blocks.simple_poly([1,2,3], a)

        alt_x =  math_blocks.simple_poly([1,2,3], x)
        alt_x_2 =  math_blocks.simple_poly([1,1,3], x)
        
        self.assertEqual(False, main_poly == p)
        self.assertEqual(True, main_poly == alt_x)
        self.assertEqual(False, main_poly == alt_x_2)

    def test_chain_eq(self):
        x = math_blocks.variable("x")
        main_poly = math_blocks.simple_poly([1,2,3], x)
        c = math_blocks.chain([1,3,2])

        self.assertEqual(False, main_poly == c)

    def test_complex_eq(self):
        x = math_blocks.variable("x")
        main_poly = math_blocks.simple_poly([1,2,3], x)
        alt_cx_1 = math_blocks.complex_number(1,2)

        self.assertEqual(False, main_poly == alt_cx_1)

    def test_exponential_eq(self):
        x = math_blocks.variable("x")
        main_poly = math_blocks.simple_poly([1,2,3], x)
        e = math_blocks.exponential(1,2)

        self.assertEqual(False, main_poly == e)


    def test_exp_eq(self):
        x = math_blocks.variable("x")
        main_poly = math_blocks.simple_poly([1,2,3], x)
        alt_fr = math_blocks.logarithm(1,2, sign=False)

        self.assertEqual(False, main_poly == alt_fr)
        
if __name__ == '__main__':
    unittest.main()
