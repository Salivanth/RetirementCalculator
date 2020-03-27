import unittest
from RetirementCalculator.calculate_tax import calculate_tax


class TestCalculateTax(unittest.TestCase):

    def test_calculate_tax_below_tax_free_threshold(self):
        tax_payable = calculate_tax(0)
        self.assertEqual(tax_payable, 0)

    def test_calculate_tax_at_tax_free_threshold(self):
        tax_payable = calculate_tax(18200)
        self.assertEqual(tax_payable, 0)

    def test_calculate_tax_just_above_tax_free_threshold(self):
        tax_payable = calculate_tax(19200)
        self.assertAlmostEqual(tax_payable, 190)

    def test_calculate_tax_at_low_threshold(self):
        tax_payable = calculate_tax(60000)
        self.assertAlmostEqual(tax_payable, 11047)

    def test_calculate_tax_at_medium_threshold(self):
        tax_payable = calculate_tax(100000)
        self.assertAlmostEqual(tax_payable, 25497)

    def test_calculate_tax_just_at_highest_threshold(self):
        tax_payable = calculate_tax(180000)
        self.assertAlmostEqual(tax_payable, 56796)

    def test_calculate_tax_above_highest_threshold(self):
        tax_payable = calculate_tax(280000)
        self.assertAlmostEqual(tax_payable, 103296)
