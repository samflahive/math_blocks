import unittest

from math_blocks.algebra.core import Number, Product


class number_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_n = Number(3)
        n = Number(3)
        n2 = Number(2)
        n3 = 3
        self.assertEqual(True, main_n == n)
        self.assertEqual(False, main_n == -n)
        self.assertEqual(False, main_n == n2)
        self.assertEqual(True, main_n == n3)


    def test_product_eq(self):
        main_n = Number(3)
        p = Product([1,2,3])
        self.assertEqual(False, main_n == p)


        
if __name__ == '__main__':
    unittest.main()
