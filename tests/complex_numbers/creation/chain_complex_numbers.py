import unittest

from math_blocks.complex_numbers import complex_number
from math_blocks.chains import chain


class chain_complex_test(unittest.TestCase):
     def test_chain_latex(self):
          c1 = complex_number(chain([3,2]),2)
          self.assertEqual(c1.latex(), "(3+2)+2i")
          c2= complex_number(-2,-chain([2,2]), sign=False)
          self.assertEqual(c2.latex(), "-(-2+(-(2+2))i)")

     def test_chain_eval(self):
          c1 = complex_number(chain([3,2]),2)
          self.assertEqual(c1.evaluate(), complex((3+2),2))
          c2= complex_number(-2,-chain([2,2]), sign=False)
          self.assertEqual(c2.evaluate(), -complex(-2,-4))


if __name__ == '__main__':
    unittest.main()
