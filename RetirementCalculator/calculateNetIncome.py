from RetirementCalculator.calculateSalarySacrifice import *
from RetirementCalculator.calculateStudentLoans import *
from RetirementCalculator.calculateTax import *


# Given a gross income, calculates net income after taxes, student loans, and salary sacrifice.
def calculate_net_income(gross_annual_income, current_student_loans):
    net_annual_income = gross_annual_income
    net_annual_income -= calculate_tax(gross_annual_income)
    net_annual_income -= calculate_student_loans(gross_annual_income, current_student_loans)
    net_annual_income -= calculate_salary_sacrifice(gross_annual_income)
    return net_annual_income
