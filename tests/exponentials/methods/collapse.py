import unittest

from math_blocks.exponentials import exponential

class collapse_exponential_test(unittest.TestCase):
    def test_exponential_ripple(self):
        ch = exponential(3,2,  sign=False)
        
        col = ch.collapse_numbers()
        
        self.assertEqual(col.latex(), "-9")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

        


if __name__ == '__main__':
    unittest.main()


