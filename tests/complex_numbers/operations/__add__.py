import unittest

from math_blocks.algebra.exponentials import ComplexNumber


class complex_add(unittest.TestCase):


    def test_complex_eq(self):
        main_cx = ComplexNumber(2,3)
        a = ComplexNumber(2,3)

        result = main_cx + a
        
        result_latex = "(2+2)+(3+3)i"
        result_value = complex(4,6)
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

        result = main_cx - a
        
        result_latex = "(2-2)+(3-3)i"
        result_value = complex(0,0)
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


if __name__ == '__main__':
    unittest.main()
