import unittest
from RetirementCalculator.calculate_net_income import calculate_net_income


class TestCalculateNetIncome(unittest.TestCase):

    def test_calculate_net_income_from_low_income(self):
        net_income = calculate_net_income(60000, 60000, 50000)
        self.assertEqual(net_income, 37020.5)

    def test_calculate_net_income_from_low_income_and_no_student_loans(self):
        net_income = calculate_net_income(60000, 60000, 0)
        self.assertEqual(net_income, 38820.5)

    def test_calculate_net_income_from_medium_income(self):
        net_income = calculate_net_income(100000, 100000, 50000)
        self.assertEqual(net_income, 60815.5)

    def test_calculate_net_income_from_medium_income_and_no_student_loans(self):
        net_income = calculate_net_income(100000, 100000, 0)
        self.assertEqual(net_income, 67815.5)

    def test_calculate_net_income_from_high_income(self):
        net_income = calculate_net_income(280000, 280000, 50000)
        self.assertEqual(net_income, 148704)

    def test_calculate_net_income_from_high_income_and_no_student_loans(self):
        net_income = calculate_net_income(280000, 280000, 0)
        self.assertEqual(net_income, 176704)
