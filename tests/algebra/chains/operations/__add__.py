import unittest

from math_blocks.algebra.core import Chain, Number


class chain_add(unittest.TestCase):

    
    def test_chain_add(self):
        main_chain = Chain([1,2,3])
        n = Number(4)

        result = main_chain + n
        
        result_latex = "1+2+3+4"
        result_value = 10
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


if __name__ == '__main__':
    unittest.main()
