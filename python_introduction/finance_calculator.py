# finance_calculator.py

# Prompt for user input with exact expected prompts
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings using expected variable names
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
