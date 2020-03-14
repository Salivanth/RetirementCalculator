import unittest
from RetirementCalculator.calculateSalarySacrifice import *


class TestCalculateSalarySacrifice(unittest.TestCase):

    def test_calculate_salary_sacrifice_from_zero_eligible_income(self):
        super_contribution = calculate_salary_sacrifice(0)
        self.assertEqual(super_contribution, 2083)

    def test_calculate_salary_sacrifice_from_some_eligible_income(self):
        super_contribution = calculate_salary_sacrifice(120000)
        self.assertEqual(super_contribution, 1133)

    def test_calculate_salary_sacrifice_from_maxed_out_income(self):
        super_contribution = calculate_salary_sacrifice(1000000)
        self.assertEqual(super_contribution, 0)