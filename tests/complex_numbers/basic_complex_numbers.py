import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.complex_numbers import complex_number

class basic_complex_test(unittest.TestCase):
     def test_basic_latex(self):
          c1 = complex_number(3,2)
          self.assertEqual(c1.latex(), "3+2i")
          c2= complex_number(-2,-2, sign=False)
          self.assertEqual(c2.latex(), "-(-2-2i)")

     def test_basic_eval(self):
          c1 = complex_number(3,2)
          self.assertEqual(c1.evaluate(), 3+2j)
          c2= complex_number(-2,-2, sign=False)
          self.assertEqual(c2.evaluate(), -(-2-2j))


if __name__ == '__main__':
    unittest.main()
