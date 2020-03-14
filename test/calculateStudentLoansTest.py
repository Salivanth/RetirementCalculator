import unittest
from RetirementCalculator.calculateStudentLoans import *


class TestCalculateStudentLoans(unittest.TestCase):

    def test_calculate_student_loans_from_zero_income(self):
        student_loan_repayment = calculate_student_loans(0, 100000)
        self.assertEqual(student_loan_repayment, 0)

    def test_calculate_student_loans_at_low_threshold(self):
        student_loan_repayment = calculate_student_loans(50000, 100000)
        self.assertEqual(student_loan_repayment, 500)

    def test_calculate_student_loans_at_middle_threshold(self):
        student_loan_repayment = calculate_student_loans(76000, 100000)
        self.assertEqual(student_loan_repayment, 3800)

    def test_calculate_student_loans_at_high_threshold(self):
        student_loan_repayment = calculate_student_loans(150000, 100000)
        self.assertEqual(student_loan_repayment, 15000)

    def test_calculate_student_loans_at_no_loan_remaining(self):
        student_loan_repayment = calculate_student_loans(150000, 0)
        self.assertEqual(student_loan_repayment, 0)

    def test_calculate_student_loans_with_partial_payment_remaining(self):
        student_loan_repayment = calculate_student_loans(150000, 10000)
        self.assertEqual(student_loan_repayment, 10000)
