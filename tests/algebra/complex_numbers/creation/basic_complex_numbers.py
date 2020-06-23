import unittest

from math_blocks.algebra.exponentials import ComplexNumber

class basic_complex_test(unittest.TestCase):
    def test_basic_latex(self):
        c1 = ComplexNumber(3,2)
        self.assertEqual(c1.latex(), "3+2i")
        c2= ComplexNumber(-2,-2, sign=False)
        self.assertEqual(c2.latex(), "-(-2-2i)")

    def test_basic_eval(self):
        c1 = ComplexNumber(3,2)
        self.assertEqual(c1.evaluate(), 3+2j)
        c2= ComplexNumber(-2,-2, sign=False)
        self.assertEqual(c2.evaluate(), 2+2j)

if __name__ == '__main__':
    unittest.main()
