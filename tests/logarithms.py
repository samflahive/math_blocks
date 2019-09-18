import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from math_blocks.logarithms import logarithm


class basic_logarithm(unittest.TestCase):
    def test_basic_latex(self):
        basic_log_A = logarithm(100,10)
        self.assertEqual(basic_log_A.latex(), "log_{10}(100)")
        basic_log_B = logarithm(4,2)
        self.assertEqual(basic_log_B.latex(), "log_{2}(4)")
        

    def test_basic_evaluation(self):
        basic_log_A = logarithm(100,10)
        self.assertAlmostEqual(basic_log_A.evaluate(), 2)
        basic_log_B = logarithm(4,2)
        self.assertAlmostEqual(basic_log_B.evaluate(), 2)
        
    def test_basic_operations(self):
        basic_log_a = logarithm(1000,10)
        basic_log_b = logarithm(100, 10)
        
        # add and subtract two logs (same base)
        basic_log_c = basic_log_a - basic_log_b
        basic_log_d = basic_log_a + basic_log_c

        self.assertEqual(basic_log_c.latex(), "log_{10}(10)")
        self.assertAlmostEqual(basic_log_c.evaluate(), 1)

        self.assertEqual(basic_log_d.latex(), "log_{10}(10000)")
        self.assertAlmostEqual(basic_log_d.evaluate(), 4)

        # add and subtract two logs (different base)
        basic_log_e = logarithm(125, 5)
        basic_log_f = logarithm(27, 3)

        log_chain_a = basic_log_d - basic_log_e
        log_chain_b = basic_log_d - basic_log_f

        self.assertEqual(log_chain_a.latex(), "log_{10}(10000)-log_{5}(125)")
        self.assertAlmostEqual(log_chain_a.evaluate(), 1)

        self.assertEqual(log_chain_b.latex(), "log_{10}(10000)-log_{3}(27)")
        self.assertAlmostEqual(log_chain_a.evaluate(), 1)
        # multiply logs

        basic_log_g = logarithm(10000, 100) * logarithm(100, 10)
        prod_log_a = basic_log_a * basic_log_b

        self.assertAlmostEqual(prod_log_a.evaluate(), basic_log_a.evaluate()*basic_log_b.evaluate())
        self.assertEqual(prod_log_a.latex(), "{} \cdot {}".format(basic_log_a.latex(), basic_log_b.latex()))
              

        # divide logs
        frac_log_a = basic_log_e / basic_log_f
        self.assertAlmostEqual(frac_log_a.evaluate(), basic_log_e.evaluate() / basic_log_f.evaluate())
        self.assertEqual(frac_log_a.latex(), "\\frac{{{0}}}{{{1}}}".format(basic_log_e.latex(), basic_log_f.latex()))
        # all operations with numbers and logs
        pl = basic_log_a + 4
        self.assertEqual(pl.latex(), "{}+4".format(basic_log_a.latex()))

        sb = 5 - basic_log_a
        self.assertEqual(sb.latex(), "5-{}".format(basic_log_a.latex()))

        dv = 11 / basic_log_a
        self.assertEqual(dv.latex(), "\\frac{11}{{{0}}}".format(basic_log_a.latex()))

        pr = 3 * basic_log_b
        self.assertEqual(or.latex(), "3 \cdot {}".format(basic_log_b.latex()))

        



if __name__ == "__main__":
    unittest.main()
