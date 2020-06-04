import unittest

from math_blocks.complex_numbers import complex_number
from math_blocks.logarithms import logarithm
from math import log

class logarithm_complex_test(unittest.TestCase):
     def test_logarithm_latex(self):
          c1 = complex_number(3,logarithm(3,2))
          self.assertEqual(c1.latex(), "3+(log_{2}3)i")
          c2= complex_number(-2,-logarithm(3,2), sign=False)
          self.assertEqual(c2.latex(), "-(-2+(-log_{2}3)i)")

     def test_logarithm_eval(self):
          c1 = complex_number(3,logarithm(3,2))
          self.assertEqual(c1.evaluate(), complex(3, log(3,2)))
          
          c2= complex_number(-2,-logarithm(3,2), sign=False)
          self.assertEqual(c2.evaluate(), complex(2,log(3,2)))


if __name__ == '__main__':
    unittest.main()
