STUDENT_LOAN_REPAYMENT_THRESHOLDS = [0, 45881, 52974, 56152, 59522, 63093, 66878, 70891, 75145, 79653, 84433, 89499,
                                     94869, 100561, 106594, 112990, 119770, 126956, 134573]
STUDENT_LOAN_REPAYMENT_TOTALS = [0, 0.01, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055, 0.06, 0.065, 0.07, 0.075,
                                 0.08, 0.085, 0.09, 0.095, 0.1]


def calculate_student_loans(annual_income, current_student_loans):
    student_loan_threshold = calculate_student_loan_threshold(annual_income)
    student_loan_repayment = annual_income * STUDENT_LOAN_REPAYMENT_TOTALS[student_loan_threshold]
    return min(student_loan_repayment, current_student_loans)


def calculate_monthly_student_loan_payment(annual_income, current_student_loans):
    student_loan_repayment = calculate_student_loans(annual_income, current_student_loans) / 12
    return min(student_loan_repayment, current_student_loans)


def calculate_student_loan_threshold(income):
    for i in range(1, len(STUDENT_LOAN_REPAYMENT_THRESHOLDS)):
        if income < STUDENT_LOAN_REPAYMENT_THRESHOLDS[i]:
            return i - 1
    return len(STUDENT_LOAN_REPAYMENT_THRESHOLDS) - 1
