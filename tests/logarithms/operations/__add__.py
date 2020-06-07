import unittest

import math_blocks


class log_add(unittest.TestCase):

    
    def test_number_add(self):
        main_log = math_blocks.logarithm(9,3)
        n = math_blocks.number(3)

        result = main_log + n
        
        result_latex = "log_{3}9+3"
        result_value = 5
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)

    def test_variable_add(self):
        main_log = math_blocks.logarithm(9,3)
        v = math_blocks.variable("v", value=3)

        result = main_log + v
        
        result_latex = "log_{3}9+v"
        result_value = 5
        
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)


    def test_product_add(self):
        main_log = math_blocks.logarithm(9,3)
        p = math_blocks.product([1,2,3])

        result = main_log + p
        
        result_latex = "log_{3}9+(1 \cdot 2 \cdot 3)"
        result_value = 8
        
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)


    def test_poly_eq(self):
        main_log = math_blocks.logarithm(9,3)
        a = math_blocks.variable("a", value=1)
        p = math_blocks.simple_poly([1,2,3], a)

        result = main_log + p
        
        result_latex = "log_{3}9+(1a^{2}+2a+3)"
        result_value = 8
        
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)

    def test_chain_eq(self):
        main_log = math_blocks.logarithm(9,3)
        alt_chain_b = math_blocks.chain([1,3,2])

        result = main_log + alt_chain_b
        
        result_latex = "log_{3}9+(1+3+2)"
        result_value = 8
        
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)

    def test_fraction_eq(self):
        main_log = math_blocks.logarithm(9,3)
        alt_log = math_blocks.logarithm(27, 3)

        result = main_log + alt_log
        
        result_latex = "log_{3}243"
        result_value = 5
        
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)

        result = main_log - alt_log
        
        #result_latex = "log_{3}0.3333"
        result_value = -1
        
        #self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)


if __name__ == '__main__':
    unittest.main()
