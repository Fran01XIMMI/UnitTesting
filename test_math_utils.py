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


    def test_subtract(self):
        """
        Just subtracts two numbers.
        """
        self.assertEqual(MathUtils.subtract(1, 2), -1)
        self.assertEqual(MathUtils.subtract(1.5, 2.5), -1.0)
        self.assertEqual(MathUtils.subtract(1, 1), 0)
        self.assertEqual(MathUtils.subtract(7, 3), 4)


    def test_divide(self):
        """
        Just divides two numbers.
        """
        self.assertEqual(MathUtils.divide(20, 5), 4)
        self.assertEqual(MathUtils.divide(4, 2), 2)
        self.assertEqual(MathUtils.divide(10, 2), 5)
        self.assertEqual(MathUtils.divide(9, 3), 3.0)

    def test_multiply(self):
        """
        Just multiply two numbers
        """
        self.assertEqual(MathUtils.multiply(10, 2), 20)
        self.assertEqual(MathUtils.multiply(9, 3), 27.0)
        self.assertEqual(MathUtils.multiply(4, 2), 8.0)
        self.assertEqual(MathUtils.multiply(2, 1), 2)
    
    def test_exponent(self):
        """
        Just exponent the numbers 
        """
        self.assertEqual(MathUtils.exponent(2, 1), 2)
        self.assertEqual(MathUtils.exponent(4, 2), 16.0)
        self.assertEqual(MathUtils.exponent(10, 2), 100)
        self.assertEqual(MathUtils.exponent(9, 3), 729.0)

    def test_mod(self):
        """
        testing the mod of two numbers
        """
        self.assertEqual(MathUtils.mod(2,1), 0)
        self.assertEqual(MathUtils.mod(4,2), 0)
        self.assertEqual(MathUtils.mod(10, 3), 1)
        self.assertEqual(MathUtils.mod(16, 3), 1.0)
    
    def test_add_paramtrized(self):
        """
        testing the parameter of the numbers
        """
        test_classes = [(3,2,5), (-1,1,0), (0,0,0), (10,-10,0)]
        for a, b, expected in test_classes:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(MathUtils.add(a,b), expected)