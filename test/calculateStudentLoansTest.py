import unittest
from RetirementCalculator.calculateStudentLoans import *


class TestCalculateStudentLoans(unittest.TestCase):

    def test_calculate_student_loans_from_zero_income(self):
        student_loan_repayment = calculate_student_loans(0)
        self.assertEqual(student_loan_repayment, 0)

    def test_calculate_student_loans_at_low_threshold(self):
        student_loan_repayment = calculate_student_loans(50000)
        self.assertEqual(student_loan_repayment, 500)

    def test_calculate_student_loans_at_middle_threshold(self):
        student_loan_repayment = calculate_student_loans(76000)
        self.assertEqual(student_loan_repayment, 3800)

    def test_calculate_student_loans_at_high_threshold(self):
        student_loan_repayment = calculate_student_loans(150000)
        self.assertEqual(student_loan_repayment, 15000)
