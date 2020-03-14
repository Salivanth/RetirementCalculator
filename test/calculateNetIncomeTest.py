import unittest
from RetirementCalculator.calculateNetIncome import *


class TestCalculateNetIncome(unittest.TestCase):

    def test_calculate_net_income_from_low_income(self):
        net_income = calculate_net_income(60000, 50000)
        self.assertEqual(net_income, 27853)

    def test_calculate_net_income_from_low_income_and_no_student_loans(self):
        net_income = calculate_net_income(60000, 0)
        self.assertEqual(net_income, 29653)

    def test_calculate_net_income_from_medium_income(self):
        net_income = calculate_net_income(100000, 50000)
        self.assertEqual(net_income, 52003)

    def test_calculate_net_income_from_medium_income_and_no_student_loans(self):
        net_income = calculate_net_income(100000, 0)
        self.assertEqual(net_income, 59003)

    def test_calculate_net_income_from_high_income(self):
        net_income = calculate_net_income(280000, 50000)
        self.assertEqual(net_income, 148704)

    def test_calculate_net_income_from_high_income_and_no_student_loans(self):
        net_income = calculate_net_income(280000, 0)
        self.assertEqual(net_income, 176704)

