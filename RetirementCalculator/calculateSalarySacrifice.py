SUPERANNUATION_CONTRIBUTION_CAP = 25000
MONTHLY_SUPER_CONTRIBUTION = SUPERANNUATION_CONTRIBUTION_CAP / 12
EMPLOYER_MANDATED_CONTRIBUTION = 0.095


# Calculate how much you should salary sacrifice to meet the optimum monthly super cap after employer contributions.
def calculate_salary_sacrifice(eligible_annual_salary):
    employer_contribution = eligible_annual_salary / 12 * EMPLOYER_MANDATED_CONTRIBUTION
    total_contribution = MONTHLY_SUPER_CONTRIBUTION - employer_contribution
    return max(0, total_contribution)
