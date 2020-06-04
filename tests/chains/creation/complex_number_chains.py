import unittest

from math_blocks.chains import chain
from math_blocks.complex_numbers import complex_number


class complex_chain_test(unittest.TestCase):
    def test_complex_latex(self):
        ch = chain([3, complex_number(3,2)])
        self.assertEqual(ch.latex(), "3+(3+2i)")
        
        ch2 = chain([-2, complex_number(3, 2, sign=False)])
        self.assertEqual(ch2.latex(), "-2-(3+2i)")

        ch3 = chain([complex_number(3, 2, sign=False), complex_number(3, 2, sign=False)])
        self.assertEqual(ch3.latex(), "-(3+2i)-(3+2i)")
        
    def test_complex_eval(self):
        ch = chain([3, complex_number(3,2)])
        self.assertEqual(ch.evaluate(), 6+2j)
        
        ch2 = chain([-2, complex_number(3, 2, sign=False)])
        self.assertEqual(ch2.evaluate(), -5-2j)

        ch3 = chain([complex_number(3, 2, sign=False), complex_number(3, 2, sign=False)])
        self.assertEqual(ch3.evaluate(), -6-4j)

if __name__ == '__main__':
    unittest.main()
