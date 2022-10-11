# compound interest
ir = 0.04
n = 1
t = 1
p = float(input("Enter your savings account balance: "))
while t <=5 :
    a = p * (1+ ir/n) ** t
    t = t + 1
    print("%.3f" %a)