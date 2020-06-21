import unittest

from math_blocks.algebra.exponentials import Exponential

class collapse_exponential_test(unittest.TestCase):
    def test_exponential_num(self):
        ch = Exponential(3,Exponential(2,1), sign=False)
        
        col = ch.to_number()
        
        self.assertEqual(col.latex(), "-9")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

        


if __name__ == '__main__':
    unittest.main()


