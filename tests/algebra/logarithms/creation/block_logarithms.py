import unittest

from math_blocks.algebra.exponentials import Logarithm, Exponential


class block_logarithm_test(unittest.TestCase):
    def test_block_latex(self):
        loga = Logarithm(Exponential(2,3),2)
        self.assertEqual(loga.latex(), "log_{2}2^{3}")

    def test_block_eval(self):
        loga = Logarithm(Exponential(2,3),2)
        self.assertAlmostEqual(loga.evaluate(), 3)


if __name__ == '__main__':
    unittest.main()

