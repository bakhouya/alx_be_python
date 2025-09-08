

# =========================================================================================
# ask the user for their monthly income and convert it to an integer
monthly_income = int(input("Enter your monthly income: "))

# ask the user for their total monthly expenses and convert it to an integer
monthly_expenses = int(input("Enter your total monthly expenses: "))

# calculate monthly savings by subtracting expenses from income
monthly_savings = monthly_income - monthly_expenses
# =========================================================================================

# =========================================================================================
# calculate projected annual savings with a simple 5% interest
# first calculate total savings for 12 months, then add 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
# =========================================================================================

# =========================================================================================
# print monthly savings
print(f"Your monthly savings are ${monthly_savings}.")

# print projected savings after one year including interest
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
# =========================================================================================
