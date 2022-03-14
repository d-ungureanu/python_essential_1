import unittest

from calculator import Calculator


class CalculatorTesting(unittest.TestCase):
    calculator = Calculator()

    def test_add(self):
        real_value = self.calculator.add(2, 6)
        expected_value = 8
        self.assertEqual(real_value, expected_value)

    def test_subtract(self):
        real_value = self.calculator.subtract(2, 6)
        expected_value = -4
        self.assertEqual(real_value, expected_value)

    def test_divide(self):
        real_value = self.calculator.divide(6, 2)
        expected_value = 3
        self.assertEqual(real_value, expected_value)

        real_value_2 = self.calculator.divide(6, 0)
        expected_value_2 = None
        self.assertEqual(real_value_2, expected_value_2)
