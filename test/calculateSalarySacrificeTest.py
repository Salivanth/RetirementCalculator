import unittest
from RetirementCalculator.calculateSalarySacrifice import *


class TestCalculateSalarySacrifice(unittest.TestCase):

    def test_calculate_salary_sacrifice_from_zero_eligible_income(self):
        super_contribution = calculate_salary_sacrifice(0)
        self.assertEqual(super_contribution, 25000)

    def test_calculate_salary_sacrifice_from_low_eligible_income(self):
        super_contribution = calculate_salary_sacrifice(60000)
        self.assertEqual(super_contribution, 19300)

    def test_calculate_salary_sacrifice_from_some_eligible_income(self):
        super_contribution = calculate_salary_sacrifice(100000)
        self.assertEqual(super_contribution, 15500)

    def test_calculate_salary_sacrifice_from_maxed_out_income(self):
        super_contribution = calculate_salary_sacrifice(1000000)
        self.assertEqual(super_contribution, 0)
