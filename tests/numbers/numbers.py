import unittest

from math_blocks.algebra.core import Number


class basic_number(unittest.TestCase):
         def test_basic_latex(self):
                  n = Number(5)
                  self.assertEqual(n.latex(), "5")

                  n2 = Number(-5)
                  self.assertEqual(n2.latex(), "-5")

                  n3 = Number(-5, sign=False)
                  self.assertEqual(n3.latex(), "5")

                  n4 = Number(4.5, sign=False)
                  self.assertEqual(n4.latex(), "-4.5")

         def test_basic_eval(self):
                  n = Number(5)
                  self.assertEqual(n.evaluate(), 5)

                  n2 = Number(-5)
                  self.assertEqual(n2.evaluate(), -5)

                  n3 = Number(-5, sign=False)
                  self.assertEqual(n3.evaluate(), 5)

                  n4 = Number(4.5, sign=False)
                  self.assertEqual(n4.evaluate(), -4.5)


    
if __name__ == '__main__':
    unittest.main()
