from RetirementCalculator.calculateNetIncome import *

ANNUAL_GROWTH_RATE = 0.07
ANNUAL_INFLATION_RATE = 0.03
MONTHLY_GROWTH_RATE = (1 + ANNUAL_GROWTH_RATE) ** (1.0/12.0)
MONTHLY_INFLATION_RATE = (1 + ANNUAL_INFLATION_RATE) ** (1.0/12.0)
WITHDRAWAL_RATE = 0.04


def main_calculation(current_savings, current_salary, current_compensation_package,
                     current_student_loans, current_expenses):

    goal_savings = current_expenses / WITHDRAWAL_RATE
    months = 0
    total_savings = current_savings

    while total_savings < goal_savings and months < 1000:
        months += 1
        total_savings *= MONTHLY_GROWTH_RATE
        goal_savings *= MONTHLY_INFLATION_RATE

        net_income = calculate_monthly_net_income(current_salary, current_compensation_package, current_student_loans)
        current_student_loans -= calculate_student_loans(current_salary, current_student_loans)

        expenses = current_expenses / 12
        total_savings += (net_income - expenses)

    print(str(months))
    print(str(total_savings) + " / " + str(goal_savings))


main_calculation(100000, 104000, 104000, 20000, 28000)
