import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from math_blocks.complex_numbers import complex_number
from math_blocks.variables import variable
from math_blocks.fractions import fraction

class basic_complex(unittest.TestCase):
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

         def test_variable_latex(self):
                  x = variable("x")
                  c1 = complex_number(3,x)
                  self.assertEqual(c1.latex(), "3+xi")

                  
                  y = variable("y", sign=False)
                  c2 = complex_number(-2, y, sign=False)
                  self.assertEqual(c2.latex(), "-(-2-yi)")

         def test_variable_eval(self):
                  x = variable("x", value=3)
                  c1 = complex_number(3,x)
                  self.assertEqual(c1.evaluate(), 3+3j)

                  
                  y = variable("y", value=2, sign=False)
                  c2 = complex_number(-2, y, sign=False)
                  self.assertEqual(c2.evaluate(), -(-2-2j))

         def test_fraction_latex(self):
                  f1 = fraction(3,2)
                  c1 = complex_number(f1,f1)
                  self.assertEqual(c1.latex(), "(\\frac{3}{2})+(\\frac{3}{2})i")

                  f2 = fraction(-3,2, sign=False)
                  c1 = complex_number(f2, f2)
                  self.assertEqual(c1.latex(), "(-\\frac{-3}{2})+(-\\frac{-3}{2})i")

         def test_fraction_eval(self):
                  f1 = fraction(3,2)
                  c1 = complex_number(f1,f1)
                  self.assertEqual(c1.evaluate(), 3/2+(3j)/2)

                  f2 = fraction(-3,2, sign=False)
                  c1 = complex_number(f2, f2)
                  self.assertEqual(c1.evaluate(), 3/2+(3j)/2)



if __name__ == '__main__':
    unittest.main()
