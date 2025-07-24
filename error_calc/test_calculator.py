# test_calculator.py
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
