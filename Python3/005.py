# Bottle Deposits
sd = 0.10
bd = 0.25
small = float(input("Enter the number of Containers less or equals to a litre: "))
big = float(input("Enter the number of Containers more than a litre: "))
value = small * sd + big * bd
# your output must have a dollar sign and be 2 decimal place
print("Your total deposit will be $%.2f." %value)
