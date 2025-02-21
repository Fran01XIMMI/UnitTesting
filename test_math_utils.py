import unittest
from math_utils import MathUtils

class TestMathUtils(unittest.TestCase):
    """
    Test Class for MathUtils.
    """

    def test_add(self):
        """
        Just adds two numbers together.
        """
        self.assertEqual(MathUtils.add(1, 2), 3)
        self.assertEqual(MathUtils.add(1.5, 2.5), 4.0)
        self.assertEqual(MathUtils.add(-1, 1), 0)
        self.assertEqual(MathUtils.add(-1.5, 1.5), 0)


    def subtract(self):
        """
        Just subtracts two numbers.
        """
        self.assertEqual(MathUtils.subtract(1, 2), -1)
        self.assertEqual(MathUtils.subtract(1.5, 2.5), -1.0)
        self.assertEqual(MathUtils.subtract(-1,1), 0)
        self.assertEqual(MathUtils.subtract(-1.5, 1.5), 0.0)


    def divide(self):
        """
        Just divides two numbers.
        """
        self.assertEqual(MathUtils.divide(3, 5), 4)
        self.assertEqual(MathUtils.divide(1, 2), -1)