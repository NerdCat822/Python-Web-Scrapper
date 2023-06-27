def get_yearly_revenue(montly_revenue):
  return montly_revenue * 12

def get_yearly_expenses(montly_expenses):
  return montly_expenses * 12

def get_tax_amount(profit):
  if profit > 100000:
    return profit * 0.25
  else:
    return profit * 0.15

def apply_tax_credits(tax_amount, tax_credits):
  return tax_amount * tax_credits
  
# Don't touch anthing below this line 🙅🏻‍♂️🙅🏻‍♀️

monthly_revenue = 5500000
montly_expenses = 2700000
tax_credits = 0.01

profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(montly_expenses)

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")