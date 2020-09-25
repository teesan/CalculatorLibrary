"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 10 == calculator.multiply(2, 5)

    def test_multiplication_neg(self):
        assert -6 == calculator.multiply(-2, 3)

    def test_division(self):
        assert 23 == calculator.divide(69, 3)
    
    def test_circumference(self):
        assert 25.14 == round(calculator.circumference(8), 2)
