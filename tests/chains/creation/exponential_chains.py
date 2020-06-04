import unittest

from math_blocks.chains import chain
from math_blocks.exponentials import exponential


class exponential_chain_test(unittest.TestCase):
    def test_exponential_latex(self):
        ch = chain([3, exponential(3,2)])
        self.assertEqual(ch.latex(), "3+3^{2}")
        
        ch2 = chain([-2,exponential(3, 2, sign=False)])
        self.assertEqual(ch2.latex(), "-2-3^{2}")

        ch3 = chain([exponential(3, 2, sign=False), exponential(3, 2, sign=False)])
        self.assertEqual(ch3.latex(), "-3^{2}-3^{2}")
        
    def test_exponential_eval(self):
        ch = chain([3, exponential(3,2)])
        self.assertEqual(ch.evaluate(), 12)
        
        ch2 = chain([-2,exponential(3, 2, sign=False)])
        self.assertEqual(ch2.evaluate(), -11)

        ch3 = chain([exponential(3, 2, sign=False), exponential(3, 2, sign=False)])
        self.assertEqual(ch3.evaluate(), -18)

if __name__ == '__main__':
    unittest.main()
