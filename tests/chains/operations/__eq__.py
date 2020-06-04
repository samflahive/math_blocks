import unittest

import math_blocks


class chain_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_chain = math_blocks.chain([1,2,3])
        n = math_blocks.number(3)
        self.assertEqual(False, main_chain == n)

    def test_variable_eq(self):
        main_chain = math_blocks.chain([1,2,3])
        v = math_blocks.variable("v")
        self.assertEqual(False, main_chain == v)

    def test_product_eq(self):
        main_chain = math_blocks.chain([1,2,3])
        p = math_blocks.product([1,2,3])
        self.assertEqual(False, main_chain == p)

    def test_poly_eq(self):
        main_chain = math_blocks.chain([1,2,3])
        a = math_blocks.variable("a")
        p = math_blocks.simple_poly([1,2,3], a)
        self.assertEqual(False, main_chain == p)

    def test_chain_eq(self):
        main_chain = math_blocks.chain([1,2,3])
        alt_chain_a = math_blocks.chain([1,2,3])
        alt_chain_b = math_blocks.chain([1,3,2])

        self.assertEqual(True, main_chain == alt_chain_a)
        self.assertEqual(False, main_chain == alt_chain_b)

if __name__ == '__main__':
    unittest.main()
