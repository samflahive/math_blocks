import unittest

from math_blocks.algebra.exponentials import Exponential, Logarithm, ComplexNumber


class block_exponential_test(unittest.TestCase):
    def test_block_latex(self):
        basic_exp_A = Exponential(ComplexNumber(2,2),Logarithm(100,10)) 
        self.assertEqual(basic_exp_A.latex(), "(2+2i)^{log_{10}100}")

        basic_exp_B = -basic_exp_A
        self.assertEqual(basic_exp_B.latex(), "-(2+2i)^{log_{10}100}")

    def test_block_eval(self):
        basic_exp_A = Exponential(ComplexNumber(2,2),Logarithm(100,10)) 
        self.assertEqual(basic_exp_A.evaluate(), complex(0,8))

        basic_exp_B = -basic_exp_A
        self.assertEqual(basic_exp_B.evaluate(), complex(-0,-8))

if __name__ == "__main__":
    unittest.main()

