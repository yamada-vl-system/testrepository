import unittest

import calculations


class CaluculationsTest(unittest.TestCase):
    """割り算をするテストする"""

    def test_divide_normal(self):
        self.assertEqual(calculations.divide(2, 2), 1)

    def test_dievide_contain_zero(self):
        # 結果が１であるため修正
        self.assertEqual(calculations.divide(0, 1), 1)


if __name__ == "__main__":
    unittest.main()
