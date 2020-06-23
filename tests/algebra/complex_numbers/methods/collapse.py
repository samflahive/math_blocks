import unittest

from math_blocks.complex_numbers import complex_number

class collapse_complex_test(unittest.TestCase):
    def test_complex_ripple(self):
        ch = complex_number(3,0,  sign=False)
        
        col = ch.collapse_numbers()
        
        self.assertEqual(col.latex(), "-3")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

        


if __name__ == '__main__':
    unittest.main()


