import unittest

from math_blocks.logarithms import logarithm

class collapse_logarithm_test(unittest.TestCase):
    def test_logarithm_collapse(self):
        ch = logarithm(100,10,  sign=False)
        
        col = ch.collapse_numbers()
        
        self.assertEqual(col.latex(), "-2.0")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

        


if __name__ == '__main__':
    unittest.main()


