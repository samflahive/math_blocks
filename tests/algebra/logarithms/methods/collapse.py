import unittest

from math_blocks.algebra.exponentials import Logarithm

class collapse_logarithm_test(unittest.TestCase):
    def test_logarithm_collapse(self):
        ch = Logarithm(100,10, sign=False)
        
        col = ch.to_number()
        
        self.assertEqual(col.latex(), "-2.0")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

        


if __name__ == '__main__':
    unittest.main()


