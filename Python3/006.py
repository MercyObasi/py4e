# Tax and Tips
tax_rate = 0.05
tips_rate = 0.18
meal_cost = float(input("Please Enter the cost of the Meal: "))
tip = meal_cost * tips_rate
tax = meal_cost * tax_rate
total = meal_cost + tip + tax
print("Tax: $%.2f ,Tip: $%.2f ,Total: $%.2f"% \
      (tax,tip,total))