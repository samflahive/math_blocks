import unittest

from math_blocks.algebra.core import Number, Product


class product_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_p = Product([1,2,3])
        n = Number(2)
        self.assertEqual(False, main_p == n)


    def test_product_eq(self):
        main_p = Product([1,2,3])
        p = Product([1,2,3], sign=False)
        p2 = Product([2,1,3])
        self.assertEqual(False, main_p == p)
        self.assertEqual(False, main_p == p2)
        self.assertEqual(True, main_p == -p)


        
if __name__ == '__main__':
    unittest.main()
