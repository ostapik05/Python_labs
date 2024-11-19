from unittest import TestCase, main
from labs.lab1.bll.calculator import calculate
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))


class TestCalculator(TestCase):
    def test_addition(self):
        self.assertEqual(calculate(5, "+", 3), 8)
        self.assertEqual(calculate(-5, "+", -3), -8)
        self.assertEqual(calculate(-5, "+", 3), -2)

    def test_subtraction(self):
        self.assertEqual(calculate(10, "-", 3), 7)
        self.assertEqual(calculate(-5, "-", -3), -2)
        self.assertEqual(calculate(5, "-", 10), -5)

    def test_multiplication(self):
        self.assertEqual(calculate(4, "*", 5), 20)
        self.assertEqual(calculate(-4, "*", 5), -20)
        self.assertEqual(calculate(0, "*", 5), 0)
        self.assertEqual(calculate(-4, "*", -5), 20)

    def test_division(self):
        self.assertEqual(calculate(10, "/", 2), 5)
        self.assertEqual(calculate(-10, "/", 2), -5)
        self.assertEqual(calculate(-10, "/", -2), 5)
        with self.assertRaises(ZeroDivisionError):
            calculate(10, "/", 0)

    def test_error_handling(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, "/", 0)
        with self.assertRaises(TypeError):
            calculate(10, "+")

if __name__ == "__main__":
    from unittest import main
    main()
