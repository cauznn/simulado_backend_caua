from django.test import TestCase

from .calculator import Calculator


class CalculatorTestCase(TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(10, 4), 6)
        self.assertEqual(calc.subtract(4, 10), -6)

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(6, 7), 42)
        self.assertEqual(calc.multiply(3, 0), 0)

    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertAlmostEqual(calc.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.divide(5, 0)
