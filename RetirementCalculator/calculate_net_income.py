from RetirementCalculator.calculate_salary_sacrifice import calculate_salary_sacrifice
from RetirementCalculator.calculate_student_loans import calculate_student_loans
from RetirementCalculator.calculate_tax import calculate_tax

SALARY_SACRIFICE_TAX_RATE = 0.15


# Given a gross income, calculates net income after taxes, student loans, and salary sacrifice.
def calculate_net_income(gross_super_eligible_income, gross_annual_income, current_student_loans):
    net_annual_income = gross_annual_income
    salary_sacrifice_total = calculate_salary_sacrifice(gross_super_eligible_income)

    net_annual_income -= calculate_student_loans(gross_annual_income, current_student_loans)
    net_annual_income -= salary_sacrifice_total
    net_annual_income -= calculate_tax(gross_annual_income - salary_sacrifice_total)
    salary_sacrifice_income = salary_sacrifice_total * (1 - SALARY_SACRIFICE_TAX_RATE)
    return net_annual_income + salary_sacrifice_income


def calculate_monthly_net_income(gross_super_eligible_income, gross_annual_income, current_student_loans):
    return calculate_net_income(gross_super_eligible_income, gross_annual_income, current_student_loans) / 12
