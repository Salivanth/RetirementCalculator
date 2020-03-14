TAX_THRESHOLDS = [0, 18200, 37000, 90000, 180000]
TAX_RATES = [0, 0.19, 0.325, 0.37, 0.45]
FIXED_TAX_AMOUNTS = [0, 0, 3572, 20797, 54096]

MEDICARE_THRESHOLDS = [0, 90000, 105000, 140000]
MEDICARE_RATES = [0, 0.01, 0.0125, 0.015]


def calculate_tax(annual_income):
    threshold = calculate_threshold(annual_income, TAX_THRESHOLDS)
    variable_tax_amount = TAX_RATES[threshold] * (annual_income - TAX_THRESHOLDS[threshold])
    return FIXED_TAX_AMOUNTS[threshold] + variable_tax_amount + calculate_medicare(annual_income)


def calculate_medicare(annual_income):
    medicare_threshold = calculate_threshold(annual_income, MEDICARE_THRESHOLDS)
    return annual_income * MEDICARE_RATES[medicare_threshold]


def calculate_monthly_tax(annual_income):
    return calculate_tax(annual_income) / 12


# Get the index of the tax or medicare threshold we're going to use.
def calculate_threshold(income, threshold):
    for i in range(1, len(threshold)):
        if income < threshold[i]:
            return i - 1
    return len(threshold) - 1
