import unittest

import math_blocks

class rebase_exp_test(unittest.TestCase):
    def test_rebase(self):
        
        exp = math_blocks.exponential(100, 2, False)
        
        exp2 = exp.rebase(10)
        
        self.assertEqual(exp2.latex(), "-10^{2 \\cdot log_{10}100}")
        
        
        
        self.assertEqual(exp.evaluate(), exp2.evaluate())



if __name__ == '__main__':
    unittest.main()

