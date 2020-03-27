SUPERANNUATION_CONTRIBUTION_CAP = 25000
EMPLOYER_MANDATED_CONTRIBUTION = 0.095


# Calculate how much to salary sacrifice to meet the monthly super cap after employer contributions.
def calculate_salary_sacrifice(eligible_annual_salary):
    employer_contribution = eligible_annual_salary * EMPLOYER_MANDATED_CONTRIBUTION
    total_contribution = SUPERANNUATION_CONTRIBUTION_CAP - employer_contribution
    return max(0, total_contribution)


def calculate_monthly_salary_sacrifice(eligible_annual_salary):
    return calculate_salary_sacrifice(eligible_annual_salary) / 12
