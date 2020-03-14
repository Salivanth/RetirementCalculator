import unittest
from RetirementCalculator.calculateTax import *


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

    def test_calculate_tax_just_at_highest_threshold(self):
        tax_payable = calculate_tax(180000)
        self.assertAlmostEqual(tax_payable, 54096)

    def test_calculate_tax_above_highest_threshold(self):
        tax_payable = calculate_tax(280000)
        self.assertAlmostEqual(tax_payable, 99096)

