import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.chains import chain
from math_blocks.complex_numbers import complex_number


class complex_chain_test(unittest.TestCase):
    def test_complex_latex(self):
        ch = chain([(3, True),(complex_number(3,2), True)])
        self.assertEqual(ch.latex(), "3+(3+2i)")
        
        ch2 = chain([(-2, True),(complex_number(3, 2, sign=False), False)])
        self.assertEqual(ch2.latex(), "-2-(-(3+2i))")

        ch3 = chain([(complex_number(3, 2, sign=False), False),(complex_number(3, 2, sign=False), False)])
        self.assertEqual(ch3.latex(), "-(-(3+2i))-(-(3+2i))")
        
    def test_complex_eval(self):
        ch = chain([(3, True),(complex_number(3,2), True)])
        self.assertEqual(ch.evaluate(), 3+3+2j)
        
        ch2 = chain([(-2, True),(complex_number(3, 2, sign=False), False)])
        self.assertEqual(ch2.evaluate(), -2+(3+2j))

        ch3 = chain([(complex_number(3, 2, sign=False), False),(complex_number(3, 2, sign=False), False)])
        self.assertEqual(ch3.evaluate(), (3+2j)+(3+2j))

if __name__ == '__main__':
    unittest.main()
