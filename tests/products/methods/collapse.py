import unittest

from math_blocks.products import product

class collapse_product_test(unittest.TestCase):
    def test_product_collapse(self):
        ch = product([3,2],  sign=False)
        
        col = ch.collapse_numbers()
        
        self.assertEqual(col.latex(), "-6")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

        


if __name__ == '__main__':
    unittest.main()


