import unittest

from math_blocks.products import product
from math_blocks.variables import variable

class variable_product_test(unittest.TestCase):
    def test_variable_latex(self):
        x = variable("x", value=2)
        pr = product([x,2])
        self.assertEqual(pr.latex(), "x \\cdot 2")
        pr2 = product([-x,2])
        self.assertEqual(pr2.latex(), "-x \\cdot 2")

    def test_variable_eval(self):
        x = variable("x", value=2)
        pr = product([x,2])
        self.assertEqual(pr.evaluate(), 4)
        pr2 = product([-x,2])
        self.assertEqual(pr2.evaluate(), -4)

if __name__ == '__main__':
    unittest.main()
