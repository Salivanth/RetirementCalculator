TAX_THRESHOLDS = [0, 18200, 37000, 90000, 180000]
TAX_RATES = [0, 0.19, 0.325, 0.37, 0.45]
FIXED_TAX_AMOUNTS = [0, 0, 3572, 20797, 54096]


def calculate_tax(annual_income):
    threshold = calculate_tax_threshold(annual_income)
    variable_tax_amount = TAX_RATES[threshold] * (annual_income - TAX_THRESHOLDS[threshold])
    return FIXED_TAX_AMOUNTS[threshold] + variable_tax_amount


def calculate_monthly_tax(annual_income):
    return calculate_tax(annual_income) / 12


# Get the index of the tax threshold we're going to use.
def calculate_tax_threshold(income):
    for i in range(1, len(TAX_THRESHOLDS)):
        if income < TAX_THRESHOLDS[i]:
            return i - 1
    return len(TAX_THRESHOLDS) - 1
