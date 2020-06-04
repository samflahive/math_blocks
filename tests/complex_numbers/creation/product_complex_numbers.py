import unittest

from math_blocks.complex_numbers import complex_number
from math_blocks.products import product


class product_complex_test(unittest.TestCase):
     def test_product_latex(self):
          c1 = complex_number(product([3,2]),2)
          self.assertEqual(c1.latex(), "(3 \\cdot 2)+2i")
          c2= complex_number(-2,-product([2,2]), sign=False)
          self.assertEqual(c2.latex(), "-(-2+(-(2 \\cdot 2))i)")

     def test_product_eval(self):
          c1 = complex_number(product([3,2]),2)
          self.assertEqual(c1.evaluate(), complex(6,2))
          c2= complex_number(-2,-product([2,2]), sign=False)
          self.assertEqual(c2.evaluate(), -complex(-2,-4))


if __name__ == '__main__':
    unittest.main()
