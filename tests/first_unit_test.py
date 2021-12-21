import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_incorrectly(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculation_correctly(self):
        assert self.calc.division(self, 30, 5) == 6

    def test_division_calculation_incorrectly(self):
        assert self.calc.division(self, 30, 5) == 5

    def test_subtraction_calculation_correctly(self):
        assert self.calc.subtraction(self, 25, 5) == 20

    def test_subtraction_calculator_incorrectly(self):
        assert self.calc.subtraction(self, 25, 5) == 4

    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_calculator_incorrectly(self):
        assert self.calc.adding(self, 1, 1) == 3

