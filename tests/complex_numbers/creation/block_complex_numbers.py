import unittest

from math_blocks.algebra.core import Number, Chain
from math_blocks.algebra.exponentials import ComplexNumber

class block_complex_test(unittest.TestCase):
    def test_basic_latex(self):
        c1 = ComplexNumber(Number(2),-Chain([2,-3]))
        self.assertEqual(c1.latex(), "2-(2-3)i")



    def test_basic_latex(self):
        c1 = ComplexNumber(Number(2),-Chain([2,-3]))
        self.assertEqual(c1.evaluate(), 2+1j)

if __name__ == '__main__':
    unittest.main()
