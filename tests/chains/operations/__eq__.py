import unittest

from math_blocks.algebra.core import Chain, Number


class chain_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_chain = Chain([1,2,3])
        n = Number(3)
        self.assertEqual(False, main_chain == n)


    def test_chain_eq(self):
        main_chain = Chain([1,2,3])
        alt_chain_a = Chain([1,2,3])
        alt_chain_b = Chain([1,3,2])

        self.assertEqual(True, main_chain == alt_chain_a)
        self.assertEqual(False, main_chain == alt_chain_b)

if __name__ == '__main__':
    unittest.main()
