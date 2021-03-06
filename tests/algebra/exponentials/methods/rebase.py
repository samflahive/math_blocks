import unittest

from math_blocks.algebra.exponentials import Exponential

class rebase_exp_test(unittest.TestCase):
    def test_rebase(self):
        
        exp = Exponential(100, 2, False)
        
        exp2 = exp.rebase(10)
        
        self.assertEqual(exp2.latex(), "-10^{2 \\cdot log_{10}100}")
        
        
        self.assertEqual(exp.evaluate(), exp2.evaluate())



if __name__ == '__main__':
    unittest.main()

